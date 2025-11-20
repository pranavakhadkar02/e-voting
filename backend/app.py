from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_mail import Mail, Message
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta, timezone
import secrets
import os
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-change-this')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///evoting.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-change-this')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Mail configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)
mail = Mail(app)
CORS(app)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["100 per hour"]
)

# JWT error handlers
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({'error': 'Token has expired'}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({'error': 'Invalid token'}), 422

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({'error': 'Authorization token is required'}), 401

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    has_voted = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    otp = db.Column(db.String(6))
    otp_expires = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    party = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    vote_count = db.Column(db.Integer, default=0)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Utility functions
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def generate_otp():
    return str(secrets.randbelow(900000) + 100000)

def send_otp_email(email, otp):
    try:
        msg = Message(
            'E-Voting OTP Verification',
            recipients=[email]
        )
        msg.body = f'''
        Welcome to E-Voting System!
        
        Your OTP for verification is: {otp}
        
        This OTP will expire in 10 minutes.
        
        If you didn't request this, please ignore this email.
        '''
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Routes
@app.route('/api/register', methods=['POST'])
@limiter.limit("5 per minute")
def register():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email and password are required'}), 400
    
    email = data['email'].lower().strip()
    password = data['password']
    
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format'}), 400
    
    if len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters'}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400
    
    # Generate OTP
    otp = generate_otp()
    otp_expires = datetime.utcnow() + timedelta(minutes=10)
    
    user = User(
        email=email,
        password_hash=generate_password_hash(password),
        otp=otp,
        otp_expires=otp_expires
    )
    
    db.session.add(user)
    db.session.commit()
    
    # Send OTP email
    if send_otp_email(email, otp):
        return jsonify({'message': 'Registration successful. OTP sent to your email.'}), 201
    else:
        return jsonify({'error': 'Failed to send OTP email'}), 500

@app.route('/api/verify-otp', methods=['POST'])
@limiter.limit("10 per minute")
def verify_otp():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('otp'):
        return jsonify({'error': 'Email and OTP are required'}), 400
    
    email = data['email'].lower().strip()
    otp = data['otp']
    
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    if user.is_verified:
        return jsonify({'error': 'User already verified'}), 400
    
    if not user.otp or user.otp_expires < datetime.utcnow():
        return jsonify({'error': 'OTP expired'}), 400
    
    if user.otp != otp:
        return jsonify({'error': 'Invalid OTP'}), 400
    
    user.is_verified = True
    user.otp = None
    user.otp_expires = None
    db.session.commit()
    
    # Create access token
    access_token = create_access_token(identity=str(user.id))
    
    return jsonify({
        'message': 'Email verified successfully',
        'access_token': access_token,
        'user': {
            'id': user.id,
            'email': user.email,
            'is_admin': user.is_admin,
            'has_voted': user.has_voted
        }
    }), 200

@app.route('/api/login', methods=['POST'])
@limiter.limit("10 per minute")
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email and password are required'}), 400
    
    email = data['email'].lower().strip()
    password = data['password']
    
    user = User.query.filter_by(email=email).first()
    
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid email or password'}), 401
    
    if not user.is_verified:
        return jsonify({'error': 'Email not verified. Please verify your email first.'}), 401

    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        'message': 'Login successful',
        'access_token': access_token,
        'user': {
            'id': user.id,
            'email': user.email,
            'is_admin': user.is_admin,
            'has_voted': user.has_voted
        }
    }), 200

@app.route('/api/resend-otp', methods=['POST'])
@limiter.limit("3 per minute")
def resend_otp():
    data = request.get_json()
    
    if not data or not data.get('email'):
        return jsonify({'error': 'Email is required'}), 400
    
    email = data['email'].lower().strip()
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    if user.is_verified:
        return jsonify({'error': 'User already verified'}), 400
    
    # Generate new OTP
    otp = generate_otp()
    otp_expires = datetime.utcnow() + timedelta(minutes=10)
    
    user.otp = otp
    user.otp_expires = otp_expires
    db.session.commit()
    
    if send_otp_email(email, otp):
        return jsonify({'message': 'OTP sent successfully'}), 200
    else:
        return jsonify({'error': 'Failed to send OTP email'}), 500

@app.route('/api/candidates', methods=['GET'])
@jwt_required()
def get_candidates():
    try:
        user_id = int(get_jwt_identity())
        user = User.query.get(user_id)
        
        if not user or not user.is_verified:
            return jsonify({'error': 'User not verified'}), 401
        
        candidates = Candidate.query.all()
        candidates_data = []
        
        for candidate in candidates:
            candidates_data.append({
                'id': candidate.id,
                'name': candidate.name,
                'party': candidate.party,
                'description': candidate.description,
                'image_url': candidate.image_url
            })
        
        return jsonify({
            'candidates': candidates_data,
            'has_voted': user.has_voted
        }), 200
    except Exception as e:
        print(f"Error in get_candidates: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/vote', methods=['POST'])
@jwt_required()
@limiter.limit("1 per minute")
def cast_vote():
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    
    if not user or not user.is_verified:
        return jsonify({'error': 'User not verified'}), 401
    
    if user.has_voted:
        return jsonify({'error': 'You have already voted'}), 400
    
    data = request.get_json()
    
    if not data or not data.get('candidate_id'):
        return jsonify({'error': 'Candidate ID is required'}), 400
    
    candidate_id = data['candidate_id']
    candidate = Candidate.query.get(candidate_id)
    
    if not candidate:
        return jsonify({'error': 'Candidate not found'}), 404
    
    # Record vote
    vote = Vote(user_id=user_id, candidate_id=candidate_id)
    db.session.add(vote)
    
    # Update candidate vote count
    candidate.vote_count += 1
    
    # Mark user as voted
    user.has_voted = True
    
    db.session.commit()
    
    return jsonify({'message': 'Vote cast successfully'}), 200

@app.route('/api/admin/results', methods=['GET'])
@jwt_required()
def get_results():
    try:
        user_id = int(get_jwt_identity())
        user = User.query.get(user_id)
        
        if not user or not user.is_admin:
            return jsonify({'error': 'Admin access required'}), 403
        
        candidates = Candidate.query.order_by(Candidate.vote_count.desc()).all()
        total_votes = Vote.query.count()
        
        results = []
        for candidate in candidates:
            percentage = (candidate.vote_count / total_votes * 100) if total_votes > 0 else 0
            results.append({
                'id': candidate.id,
                'name': candidate.name,
                'party': candidate.party,
                'vote_count': candidate.vote_count,
                'percentage': round(percentage, 2)
            })
        
        return jsonify({
            'results': results,
            'total_votes': total_votes,
            'total_users': User.query.filter_by(is_verified=True).count()
        }), 200
    except Exception as e:
        print(f"Error in get_results: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/admin/candidates', methods=['POST'])
@jwt_required()
def add_candidate():
    try:
        user_id = int(get_jwt_identity())
        user = User.query.get(user_id)
        
        if not user or not user.is_admin:
            return jsonify({'error': 'Admin access required'}), 403
        
        data = request.get_json()
        
        if not data or not data.get('name') or not data.get('party'):
            return jsonify({'error': 'Name and party are required'}), 400
        
        candidate = Candidate(
            name=data['name'],
            party=data['party'],
            description=data.get('description', ''),
            image_url=data.get('image_url', 'https://via.placeholder.com/150')
        )
        
        db.session.add(candidate)
        db.session.commit()
        
        return jsonify({'message': 'Candidate added successfully'}), 201
    except Exception as e:
        print(f"Error in add_candidate: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/admin/candidates', methods=['GET'])
@jwt_required()
def get_all_candidates():
    try:
        user_id = int(get_jwt_identity())
        user = User.query.get(user_id)
        
        if not user or not user.is_admin:
            return jsonify({'error': 'Admin access required'}), 403
        
        candidates = Candidate.query.all()
        candidates_data = []
        
        for candidate in candidates:
            candidates_data.append({
                'id': candidate.id,
                'name': candidate.name,
                'party': candidate.party,
                'description': candidate.description,
                'image_url': candidate.image_url,
                'vote_count': candidate.vote_count
            })
        
        return jsonify({'candidates': candidates_data}), 200
    except Exception as e:
        print(f"Error in get_all_candidates: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/admin/candidates/<int:candidate_id>', methods=['PUT'])
@jwt_required()
def update_candidate(candidate_id):
    try:
        user_id = int(get_jwt_identity())
        user = User.query.get(user_id)
        
        if not user or not user.is_admin:
            return jsonify({'error': 'Admin access required'}), 403
        
        candidate = Candidate.query.get(candidate_id)
        if not candidate:
            return jsonify({'error': 'Candidate not found'}), 404
        
        data = request.get_json()
        
        if not data or not data.get('name') or not data.get('party'):
            return jsonify({'error': 'Name and party are required'}), 400
        
        candidate.name = data['name']
        candidate.party = data['party']
        candidate.description = data.get('description', '')
        candidate.image_url = data.get('image_url', 'https://via.placeholder.com/150')
        
        db.session.commit()
        
        return jsonify({'message': 'Candidate updated successfully'}), 200
    except Exception as e:
        print(f"Error in update_candidate: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/admin/candidates/<int:candidate_id>', methods=['DELETE'])
@jwt_required()
def delete_candidate(candidate_id):
    try:
        user_id = int(get_jwt_identity())
        user = User.query.get(user_id)
        
        if not user or not user.is_admin:
            return jsonify({'error': 'Admin access required'}), 403
        
        candidate = Candidate.query.get(candidate_id)
        if not candidate:
            return jsonify({'error': 'Candidate not found'}), 404
        
        # Check if candidate has votes
        vote_count = Vote.query.filter_by(candidate_id=candidate_id).count()
        if vote_count > 0:
            return jsonify({'error': 'Cannot delete candidate with existing votes'}), 400
        
        db.session.delete(candidate)
        db.session.commit()
        
        return jsonify({'message': 'Candidate deleted successfully'}), 200
    except Exception as e:
        print(f"Error in delete_candidate: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/user/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'user': {
            'id': user.id,
            'email': user.email,
            'is_admin': user.is_admin,
            'has_voted': user.has_voted,
            'created_at': user.created_at.isoformat()
        }
    }), 200

# Initialize database
def init_db():
    with app.app_context():
        db.create_all()
        
        # Create default admin user if none exists
        if not User.query.filter_by(is_admin=True).first():
            admin_user = User(
                email='admin@evoting.com',
                password_hash=generate_password_hash('admin123'),
                is_verified=True,
                is_admin=True
            )
            db.session.add(admin_user)
            db.session.commit()
            print("Database initialized with default admin user")
            print("Admin login: admin@evoting.com / admin123")
        else:
            print("Database initialized")

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)