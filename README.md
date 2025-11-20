# 🗳️ E-Voting System

[![GitHub license](https://img.shields.io/github/license/pranavakhadkar02/e-voting)](https://github.com/pranavakhadkar02/e-voting/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/pranavakhadkar02/e-voting)](https://github.com/pranavakhadkar02/e-voting/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/pranavakhadkar02/e-voting)](https://github.com/pranavakhadkar02/e-voting/issues)
[![GitHub forks](https://img.shields.io/github/forks/pranavakhadkar02/e-voting)](https://github.com/pranavakhadkar02/e-voting/network)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![React](https://img.shields.io/badge/React-19+-61DAFB.svg)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-4.9+-blue.svg)](https://www.typescriptlang.org/)

A **secure, modern e-voting application** built with React frontend and Python Flask backend. Features real-time voting, comprehensive admin dashboard, and enterprise-grade security.

> 🚀 **Live Demo**: [Coming Soon]  
> 📖 **Documentation**: [Setup Guide](SETUP.md) | [Contributing](CONTRIBUTING.md) | [API Docs](#api-endpoints)  
> 🎯 **Status**: Active Development | Ready for Production

## ✨ Features

### 🔐 Authentication & Security

- **Multi-factor Authentication**: Email-based registration with OTP verification
- **JWT Token System**: Secure, stateless authentication with automatic expiration
- **Password Security**: Bcrypt hashing with salt for password protection
- **Rate Limiting**: Prevents brute force attacks and spam
- **CORS Protection**: Configurable cross-origin resource sharing
- **Input Validation**: Comprehensive sanitization and validation

### 🗳️ Voting System

- **One Person, One Vote**: Strict enforcement prevents duplicate voting
- **Real-time Counting**: Live vote tallying and result updates
- **Candidate Management**: Dynamic candidate addition and management
- **Vote Integrity**: Cryptographic vote verification and storage
- **Anonymous Voting**: User privacy maintained throughout process

### 📊 Admin Dashboard

- **Comprehensive Analytics**: Detailed voting statistics and trends
- **Real-time Monitoring**: Live vote tracking and system health
- **User Management**: View and manage registered voters
- **Result Visualization**: Charts and graphs for vote distribution
- **Export Capabilities**: Download results in multiple formats
- **Audit Trail**: Complete logging of all system activities

### 🔧 Technical Features

- **Responsive Design**: Mobile-first, works on all devices
- **Progressive Web App**: Offline capability and app-like experience
- **RESTful API**: Well-documented, standardized endpoints
- **Database Flexibility**: SQLite for development, PostgreSQL for production
- **Email Integration**: Automated notifications and OTP delivery
- **Error Handling**: Comprehensive error reporting and recovery

## 🛠️ Tech Stack

### Backend (Python)

| Technology             | Version | Purpose                                 |
| ---------------------- | ------- | --------------------------------------- |
| **Flask**              | 2.3.3   | Web framework and API server            |
| **SQLAlchemy**         | 3.0.5   | Database ORM and migrations             |
| **Flask-JWT-Extended** | 4.5.3   | JWT authentication and authorization    |
| **Flask-Mail**         | 0.9.1   | Email service integration               |
| **Flask-CORS**         | 4.0.0   | Cross-origin resource sharing           |
| **Flask-Limiter**      | 3.5.0   | Rate limiting and DDoS protection       |
| **Werkzeug**           | 2.3.7   | Password hashing and security utilities |
| **SQLite/PostgreSQL**  | Latest  | Database storage (configurable)         |

### Frontend (React + TypeScript)

| Technology                | Version | Purpose                              |
| ------------------------- | ------- | ------------------------------------ |
| **React**                 | 19.2.0  | UI framework and component system    |
| **TypeScript**            | 4.9.5   | Type safety and enhanced development |
| **React Router**          | 7.9.6   | Client-side routing and navigation   |
| **Axios**                 | 1.13.2  | HTTP client for API communication    |
| **Bootstrap**             | 5.3.8   | Responsive UI components and styling |
| **React Toastify**        | 11.0.5  | Toast notifications and alerts       |
| **React Testing Library** | 16.3.0  | Component testing utilities          |

### Development & Build Tools

- **Create React App** - Frontend build toolchain
- **Python Virtual Environment** - Dependency isolation
- **npm/pip** - Package management
- **Jest** - JavaScript testing framework
- **ESLint** - Code linting and formatting

## 🚀 Quick Start

### Prerequisites

Ensure you have the following installed:

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Node.js 16+** ([Download](https://nodejs.org/))
- **Git** ([Download](https://git-scm.com/))

### 1️⃣ Clone Repository

```bash
git clone https://github.com/pranavakhadkar02/e-voting.git
cd e-voting
```

### 2️⃣ Backend Setup

```bash
cd backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your email settings (optional)
```

### 3️⃣ Frontend Setup

```bash
cd ../frontend

# Install dependencies
npm install

# Verify installation
npm list --depth=0
```

### 4️⃣ Run the Application

**Terminal 1 - Backend:**

```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python app.py
```

**Terminal 2 - Frontend:**

```bash
cd frontend
npm start
```

### 5️⃣ Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **Admin Panel**: http://localhost:3000/admin

**Default Admin Credentials:**

- Email: `admin@evoting.com`
- Password: `admin123`

> 📝 **Need detailed setup instructions?** Check out our comprehensive [Setup Guide](SETUP.md)

## 📧 Email Configuration (Optional)

For OTP functionality, configure your email settings in `backend/.env`:

### Gmail Setup (Recommended)

1. **Enable 2-Factor Authentication** in your Google Account
2. **Generate App Password**:

   - Go to Google Account Settings
   - Security → 2-Step Verification → App passwords
   - Select app: Mail, Select device: Other
   - Copy the 16-character password

3. **Update .env file**:

```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-16-char-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
```

### Alternative Email Providers

| Provider        | SMTP Server           | Port    | TLS |
| --------------- | --------------------- | ------- | --- |
| **Outlook**     | smtp-mail.outlook.com | 587     | Yes |
| **Yahoo**       | smtp.mail.yahoo.com   | 587     | Yes |
| **Custom SMTP** | your.smtp.server      | 587/465 | Yes |

> 💡 **Note**: The application works without email configuration, but OTP verification will be disabled.

## 👤 Demo Accounts

### Admin Account

- **Email**: `admin@evoting.com`
- **Password**: `admin123`
- **Access**: Full admin dashboard, results, user management

### Test User Account

- Create new accounts through registration
- Use any valid email format for testing
- OTP will be displayed in backend console if email not configured

## 📁 Project Structure

```
e-voting/
├── 📁 backend/                    # Python Flask API Server
│   ├── 🐍 app.py                 # Main Flask application & routes
│   ├── 🧪 debug_jwt.py           # JWT debugging utilities
│   ├── 🔧 manage.py              # Database management scripts
│   ├── 📋 requirements.txt       # Python dependencies
│   ├── 🔒 .env.example          # Environment variables template
│   ├── 🗄️ evoting.db            # SQLite database (auto-generated)
│   ├── 🧪 test_*.py             # Unit tests and workflows
│   └── 📁 __pycache__/          # Python cache files
│
├── 📁 frontend/                   # React TypeScript Application
│   ├── 📁 public/               # Static assets
│   │   ├── 🌐 index.html        # HTML template
│   │   ├── 📄 manifest.json     # PWA manifest
│   │   └── 🤖 robots.txt        # SEO robots file
│   ├── 📁 src/                  # Source code
│   │   ├── 📁 components/       # Reusable UI components
│   │   │   ├── AdminLayout.tsx  # Admin dashboard layout
│   │   │   ├── Navbar.tsx       # Navigation component
│   │   │   └── ProtectedRoute.tsx # Route protection
│   │   ├── 📁 contexts/         # React context providers
│   │   │   └── AuthContext.tsx  # Authentication state
│   │   ├── 📁 pages/            # Page components
│   │   │   ├── Admin.tsx        # Admin dashboard
│   │   │   ├── Home.tsx         # Landing page
│   │   │   ├── Login.tsx        # User login
│   │   │   ├── Register.tsx     # User registration
│   │   │   ├── Vote.tsx         # Voting interface
│   │   │   ├── VerifyOTP.tsx    # OTP verification
│   │   │   └── ManageCandidates.tsx # Candidate management
│   │   ├── 📁 services/         # API communication
│   │   │   └── api.ts           # HTTP client & API calls
│   │   ├── ⚛️ App.tsx           # Main application component
│   │   ├── 🎨 App.css           # Global styles
│   │   └── 📝 index.tsx         # Application entry point
│   ├── 📦 package.json          # Node.js dependencies & scripts
│   └── ⚙️ tsconfig.json         # TypeScript configuration
│
├── 📖 README.md                   # Project documentation (this file)
├── 🛠️ SETUP.md                    # Detailed setup instructions
├── 🤝 CONTRIBUTING.md             # Contribution guidelines
└── 📄 LICENSE                     # MIT license
```

## 🔌 API Endpoints

### Authentication Endpoints

| Method | Endpoint            | Description                           | Auth Required |
| ------ | ------------------- | ------------------------------------- | ------------- |
| `POST` | `/api/register`     | User registration with email/password | ❌            |
| `POST` | `/api/verify-otp`   | Email verification with OTP code      | ❌            |
| `POST` | `/api/login`        | User authentication & JWT token       | ❌            |
| `POST` | `/api/resend-otp`   | Resend OTP to user email              | ❌            |
| `GET`  | `/api/user/profile` | Get authenticated user profile        | ✅            |

### Voting Endpoints

| Method | Endpoint                | Description                       | Auth Required |
| ------ | ----------------------- | --------------------------------- | ------------- |
| `GET`  | `/api/candidates`       | Retrieve all available candidates | ✅            |
| `POST` | `/api/vote`             | Cast vote for selected candidate  | ✅            |
| `GET`  | `/api/user/vote-status` | Check if user has already voted   | ✅            |

### Admin Endpoints

| Method | Endpoint             | Description                       | Auth Required |
| ------ | -------------------- | --------------------------------- | ------------- |
| `GET`  | `/api/admin/results` | Get comprehensive voting results  | ✅ Admin      |
| `GET`  | `/api/admin/stats`   | Get voting statistics & analytics | ✅ Admin      |
| `GET`  | `/api/admin/users`   | Get list of registered users      | ✅ Admin      |

### Response Format

All API responses follow this structure:

```json
{
  "success": true/false,
  "message": "Human readable message",
  "data": {}, // Response data (if applicable)
  "error": "Error details" // Only present on errors
}
```

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

## 🔧 Troubleshooting

### Quick Fixes

| Issue                    | Solution                                                         |
| ------------------------ | ---------------------------------------------------------------- |
| **Backend won't start**  | Check Python 3.8+, verify dependencies, ensure port 5000 is free |
| **Frontend won't start** | Check Node.js 16+, run `npm install`, ensure port 3000 is free   |
| **Email not sending**    | Verify `.env` credentials, use Gmail App Password, enable 2FA    |
| **Database errors**      | Delete `evoting.db`, restart backend, check file permissions     |
| **Import errors**        | Activate virtual environment, reinstall requirements             |
| **CORS errors**          | Check frontend URL in Flask-CORS configuration                   |

### Detailed Solutions

**🐍 Python Issues:**

```bash
# Check Python version
python3 --version

# Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**⚛️ React Issues:**

```bash
# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

**🗄️ Database Issues:**

```bash
# Reset database
rm backend/evoting.db
# Restart backend server to recreate
```

> 📚 **Need more help?** Check our detailed [Setup Guide](SETUP.md) or [create an issue](https://github.com/pranavakhadkar02/e-voting/issues/new).

## 🤝 Contributing

We welcome contributions from developers of all skill levels! Please see our [Contributing Guide](CONTRIBUTING.md) for detailed information.

### Quick Contribution Steps

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/your-username/e-voting.git`
3. **Create** feature branch: `git checkout -b feature/amazing-feature`
4. **Make** your changes and test thoroughly
5. **Commit** with clear message: `git commit -m 'Add: amazing feature'`
6. **Push** to branch: `git push origin feature/amazing-feature`
7. **Open** a Pull Request with detailed description

### Areas for Contribution

- 🐛 **Bug fixes** and security improvements
- ✨ **New features** and enhancements
- 📚 **Documentation** improvements
- 🧪 **Testing** and test coverage
- 🎨 **UI/UX** improvements
- 🌐 **Internationalization** (i18n)

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - feel free to use, modify, and distribute this software.
```

## 🙏 Acknowledgments

- **React Team** - For the amazing frontend framework
- **Flask Community** - For the lightweight and powerful backend framework
- **Open Source Contributors** - For inspiration and code contributions
- **Security Researchers** - For guidance on secure voting systems
- **Beta Testers** - For feedback and bug reports

## 📞 Support & Community

### Get Help

- 🐛 **Found a bug?** [Report it](https://github.com/pranavakhadkar02/e-voting/issues/new)
- 💡 **Have an idea?** [Request a feature](https://github.com/pranavakhadkar02/e-voting/issues/new)
- ❓ **Need help?** [Start a discussion](https://github.com/pranavakhadkar02/e-voting/discussions)
- 📖 **Documentation issues?** [Improve docs](https://github.com/pranavakhadkar02/e-voting/pulls)

### Connect with Us

- 🐙 **GitHub**: [@pranavakhadkar02](https://github.com/pranavakhadkar02)
- 💬 **Discussions**: [Project Discussions](https://github.com/pranavakhadkar02/e-voting/discussions)
- 📧 **Email**: Create an issue for direct contact

---

### 📊 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/pranavakhadkar02/e-voting)
![GitHub code size](https://img.shields.io/github/languages/code-size/pranavakhadker02/e-voting)
![GitHub last commit](https://img.shields.io/github/last-commit/pranavakhadkar02/e-voting)
![GitHub contributors](https://img.shields.io/github/contributors/pranavakhadkar02/e-voting)

⭐ **Star this repository** if you find it useful!

**Built with ❤️ using React, TypeScript, Flask, and Python**

_Developed by [Pranav Akhadkar](https://github.com/pranavakhadkar02) and the open-source community_

---

> 💡 **Pro Tip**: Set up the project locally and explore the code to better understand the architecture before contributing!
