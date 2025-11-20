# 🗳️ E-Voting System

[![GitHub license](https://img.shields.io/github/license/pranavakhadkar02/e-voting)](https://github.com/pranavakhadkar02/e-voting/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/pranavakhadkar02/e-voting)](https://github.com/pranavakhadkar02/e-voting/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/pranavakhadkar02/e-voting)](https://github.com/pranavakhadkar02/e-voting/issues)
[![GitHub forks](https://img.shields.io/github/forks/pranavakhadkar02/e-voting)](https://github.com/pranavakhadkar02/e-voting/network)

A secure, modern e-voting application built with React frontend and Python Flask backend.

> 🚀 **Live Demo**: [Coming Soon]  
> 📖 **Documentation**: [Setup Guide](SETUP.md) | [Contributing](CONTRIBUTING.md)

## Features

✅ **User Registration & Authentication**

- Email-based registration with OTP verification
- Secure login with JWT tokens
- Password hashing and validation

✅ **Voting System**

- One-vote-per-user restriction
- Secure vote storage in database
- Real-time vote counting

✅ **Admin Dashboard**

- Comprehensive voting results
- Real-time statistics
- Vote percentage and turnout rates

✅ **Security Features**

- JWT-based authentication
- Rate limiting on sensitive endpoints
- Email OTP verification
- CORS protection
- Input validation and sanitization

## Tech Stack

### Backend (Python)

- **Flask** - Web framework
- **SQLAlchemy** - Database ORM
- **Flask-JWT-Extended** - JWT authentication
- **Flask-Mail** - Email functionality
- **SQLite** - Database (easily switchable to PostgreSQL)

### Frontend (React + TypeScript)

- **React 18** - UI framework
- **TypeScript** - Type safety
- **React Router** - Navigation
- **Axios** - HTTP client
- **Bootstrap 5** - UI components
- **React Toastify** - Notifications

## Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- Git

### Backend Setup

1. **Navigate to backend directory**

   ```bash
   cd backend
   ```

2. **Create virtual environment**

   ```bash
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**

   ```bash
   cp .env.example .env
   # Edit .env file with your email settings
   ```

5. **Run the backend**
   ```bash
   python app.py
   ```
   Backend runs on: http://localhost:5000

### Frontend Setup

1. **Navigate to frontend directory**

   ```bash
   cd frontend
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm start
   ```
   Frontend runs on: http://localhost:3000

## Email Configuration

For OTP functionality, configure your email settings in `backend/.env`:

### Gmail Setup

1. Enable 2-factor authentication
2. Generate an App Password
3. Use App Password in `.env` file

```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
```

### Other Providers

- **Outlook**: smtp-mail.outlook.com, port 587
- **Yahoo**: smtp.mail.yahoo.com, port 587

## Demo Account

**Admin Access:**

- Email: `admin@evoting.com`
- Password: `admin123`

## Project Structure

```
e-voting/
├── backend/                 # Python Flask API
│   ├── app.py              # Main Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example       # Environment variables template
│   └── evoting.db         # SQLite database (auto-generated)
├── frontend/               # React application
│   ├── src/
│   │   ├── components/    # Reusable components
│   │   ├── contexts/      # React contexts
│   │   ├── pages/         # Page components
│   │   ├── services/      # API calls
│   │   └── App.tsx       # Main App component
│   ├── package.json      # Node.js dependencies
│   └── .env             # Environment variables
└── README.md            # This file
```

## API Endpoints

### Authentication

- `POST /api/register` - User registration
- `POST /api/verify-otp` - Email verification
- `POST /api/login` - User login
- `POST /api/resend-otp` - Resend OTP
- `GET /api/user/profile` - Get user profile

### Voting

- `GET /api/candidates` - Get all candidates
- `POST /api/vote` - Cast a vote

### Admin

- `GET /api/admin/results` - Get voting results (admin only)

## Development

### Adding New Candidates

Candidates are automatically seeded when you first run the backend. To add more:

1. Modify the `init_db()` function in `backend/app.py`
2. Add new candidate objects to the `candidates` array
3. Restart the backend

### Database Management

The app uses SQLite by default. To switch to PostgreSQL:

1. Install PostgreSQL
2. Update `DATABASE_URL` in `.env`
3. Install `psycopg2`: `pip install psycopg2-binary`

## Deployment

### Backend (Heroku)

1. Create `Procfile`: `web: python app.py`
2. Set environment variables
3. Deploy with Git

### Frontend (Netlify/Vercel)

1. Build: `npm run build`
2. Deploy `build/` folder
3. Set environment variables

## Security Considerations

- All passwords are hashed using Werkzeug
- JWT tokens expire after 1 hour
- Rate limiting prevents abuse
- Email OTP expires after 10 minutes
- Input validation on all endpoints
- CORS configured for security

## Troubleshooting

### Common Issues

**Backend won't start:**

- Check Python version (3.8+)
- Verify all dependencies installed
- Check port 5000 availability

**Frontend won't start:**

- Check Node.js version (16+)
- Run `npm install` again
- Check port 3000 availability

**Email not sending:**

- Verify email credentials in `.env`
- Check Gmail App Password setup
- Ensure 2FA is enabled for Gmail

**Database errors:**

- Delete `evoting.db` file and restart backend
- Check file permissions
- Verify SQLite installation

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Make changes and test thoroughly
4. Commit your changes (`git commit -m 'Add: amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with modern web technologies
- Inspired by the need for secure digital voting
- Thanks to the open-source community

## 📞 Support

- 🐛 **Found a bug?** [Report it](https://github.com/pranavakhadkar02/e-voting/issues/new?template=bug_report.yml)
- 💡 **Have an idea?** [Request a feature](https://github.com/pranavakhadkar02/e-voting/issues/new?template=feature_request.yml)
- ❓ **Need help?** [Start a discussion](https://github.com/pranavakhadkar02/e-voting/discussions)

---

⭐ **Star this repository** if you find it useful!

Built with ❤️ using React and Flask by [Pranav Akhadkar](https://github.com/pranavakhadkar02)
