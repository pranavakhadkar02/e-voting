# 🗳️ E-Voting System Setup Guide

Complete setup instructions for macOS, Windows, and Linux systems.

## 📋 Prerequisites

### System Requirements

- **Python**: 3.8 or higher
- **Node.js**: 16 or higher
- **Git**: Latest version
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space

### macOS Setup

1. **Install Homebrew** (if not already installed)

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python 3.8+**

   ```bash
   brew install python
   # Verify installation
   python3 --version
   ```

3. **Install Node.js 16+**
   ```bash
   brew install node
   # Verify installation
   node --version
   npm --version
   ```

### Windows Setup

1. **Install Python 3.8+**

   - Download from [python.org](https://www.python.org/downloads/)
   - ✅ **Important**: Check "Add Python to PATH" during installation
   - Open Command Prompt and verify: `python --version`

2. **Install Node.js 16+**

   - Download from [nodejs.org](https://nodejs.org/)
   - Run the installer with default settings
   - Open Command Prompt and verify: `node --version` and `npm --version`

3. **Install Git** (if not already installed)
   - Download from [git-scm.com](https://git-scm.com/)

### Linux Setup (Ubuntu/Debian)

1. **Update package list**

   ```bash
   sudo apt update
   ```

2. **Install Python 3.8+**

   ```bash
   sudo apt install python3 python3-pip python3-venv
   python3 --version
   ```

3. **Install Node.js 16+**
   ```bash
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install -y nodejs
   node --version && npm --version
   ```

## 🚀 Project Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/pranavakhadkar02/e-voting.git
cd e-voting
```

_Or download and extract the project files to a folder named `e-voting`._

### Step 2: Backend Setup

#### macOS/Linux

```bash
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
```

#### Windows

```cmd
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
copy .env.example .env
```

### Step 3: Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Verify installation
npm list --depth=0
```

### Step 4: Configure Email (Optional)

Edit the `.env` file in the backend directory:

```env
# Flask Configuration
SECRET_KEY=your-super-secret-key-change-this-in-production
JWT_SECRET_KEY=your-jwt-secret-key-change-this-too

# Database Configuration
DATABASE_URL=sqlite:///evoting.db

# Gmail Configuration (Optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
```

**Gmail Setup (Optional):**

1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Enable 2-factor authentication
3. Generate an App Password (App passwords → Select app → Mail)
4. Use the 16-character App Password (not your regular password)

**Other Email Providers:**

- **Outlook**: `smtp-mail.outlook.com`, port 587
- **Yahoo**: `smtp.mail.yahoo.com`, port 587

> 📝 **Note:** The app works without email configuration, but OTP verification will be disabled.

## 🏃‍♂️ Running the Application

### Method 1: Start Both Servers Simultaneously

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

### Method 2: Using npm scripts (if available)

```bash
# From project root
npm run dev  # If configured
```

### Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **Admin Panel**: http://localhost:3000/admin

### Default Admin Credentials

- **Email**: `admin@evoting.com`
- **Password**: `admin123`

## Testing the Application

1. **Open your browser** and go to http://localhost:3000

2. **Admin Login** (pre-configured):

   - Email: `admin@evoting.com`
   - Password: `admin123`

3. **Register New User**:

   - Click "Register"
   - Enter email and password
   - If email is configured, you'll receive OTP
   - If email not configured, check backend console for OTP

4. **Vote**:

   - After login/verification, go to Vote page
   - Select a candidate and vote

5. **View Results** (Admin only):
   - Login as admin
   - Go to Admin Panel to see results

## 🔧 Troubleshooting

### Python Issues

**❌ Command not found: python3 (macOS/Linux)**

```bash
# Try alternatives
python --version
which python3
# Install via Homebrew (macOS)
brew install python
# Install via apt (Ubuntu/Debian)
sudo apt install python3
```

**❌ 'python' is not recognized (Windows)**

- Reinstall Python with "Add to PATH" checked
- Or add Python to PATH manually:
  - System Properties → Environment Variables
  - Add Python installation path to PATH

**❌ Permission denied errors**

```bash
# Use --user flag
pip install --user -r requirements.txt
# Or fix permissions (macOS/Linux)
sudo chown -R $(whoami) ~/.local
```

### Node.js Issues

**❌ npm command not found**

```bash
# Verify Node.js installation
which node
which npm
# Reinstall Node.js if necessary
```

**❌ npm install fails**

```bash
# Clear npm cache
npm cache clean --force
# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Port Issues

**❌ Port already in use**

_macOS/Linux:_

```bash
# Find process using port 5000
lsof -i :5000
# Kill process
kill -9 <PID>
```

_Windows:_

```cmd
# Find process using port 5000
netstat -ano | findstr :5000
# Kill process
taskkill /PID <process-id> /F
```

### Database Issues

**❌ Database locked**

1. Stop the backend server (`Ctrl+C`)
2. Delete `backend/evoting.db` file
3. Restart backend (database will be recreated)

**❌ SQLite errors**

```bash
# Check SQLite installation
sqlite3 --version
# Install if missing (Ubuntu/Debian)
sudo apt install sqlite3
```

### Email Configuration Issues

**❌ Gmail authentication error**

- ✅ Enable 2-factor authentication
- ✅ Use App Password (16 characters)
- ✅ Check email/password for typos
- ✅ Verify Gmail allows "Less secure apps" (if not using App Password)

**❌ OTP not received**

- Check spam/junk folder
- Verify email address spelling
- Check backend console for error messages
- Try resending OTP

### Virtual Environment Issues

**❌ Virtual environment activation fails**

_macOS/Linux:_

```bash
# Ensure you're in the correct directory
pwd
source venv/bin/activate
```

_Windows:_

```cmd
# PowerShell execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

### Network & Access Issues

**❌ Can't access from other devices**

- Backend: Modify `app.py` to use `host='0.0.0.0'`
- Frontend: Start with `npm start -- --host 0.0.0.0`
- Check firewall settings
- Ensure both devices are on the same network

## 💡 Development Tips

### Hot Reload & Development Mode

- **Frontend**: Automatically reloads on file changes
- **Backend**: Use Flask development mode for auto-reload:
  ```bash
  export FLASK_ENV=development  # Linux/macOS
  set FLASK_ENV=development     # Windows
  python app.py
  ```

### Database Management

**SQLite Browser (GUI):**

```bash
# macOS
brew install --cask db-browser-for-sqlite

# Ubuntu/Debian
sudo apt install sqlitebrowser

# Windows
# Download from: https://sqlitebrowser.org/
```

**Command Line:**

```bash
# Open database
sqlite3 backend/evoting.db
# List tables
.tables
# Exit
.quit
```

### API Testing Tools

- **Postman** - Full-featured API client
- **Thunder Client** - VS Code extension
- **curl** - Command line HTTP client
- **Browser DevTools** - Network tab for debugging

### Recommended IDE Setup

**VS Code Extensions:**

- Python
- ES7+ React/Redux/React-Native snippets
- TypeScript and JavaScript Language Features
- Thunder Client (API testing)
- SQLite Viewer

**Alternative IDEs:**

- **PyCharm** - Python development
- **WebStorm** - React/TypeScript development

### Project Structure Understanding

```
e-voting/
├── backend/              # Flask API server
│   ├── app.py           # Main application
│   ├── requirements.txt # Python dependencies
│   ├── .env            # Environment variables
│   └── evoting.db      # SQLite database
├── frontend/            # React application
│   ├── src/
│   │   ├── components/ # Reusable UI components
│   │   ├── contexts/   # React context providers
│   │   ├── pages/      # Page components
│   │   └── services/   # API service functions
│   └── package.json   # Node.js dependencies
└── docs/              # Documentation
```

## 🚀 Quick Start Checklist

- [ ] **Prerequisites installed**: Python 3.8+, Node.js 16+, Git
- [ ] **Repository cloned**: `git clone <repo-url>`
- [ ] **Backend setup**: Virtual environment created and activated
- [ ] **Dependencies installed**: `pip install -r requirements.txt`
- [ ] **Environment configured**: `.env` file created from `.env.example`
- [ ] **Frontend setup**: `npm install` completed successfully
- [ ] **Backend running**: `python app.py` on port 5000
- [ ] **Frontend running**: `npm start` on port 3000
- [ ] **Admin access**: Can login with admin@evoting.com / admin123
- [ ] **User registration**: Can create new user account
- [ ] **Voting works**: Can cast and view votes

## 🆘 Getting Help

If you encounter issues:

1. **Check this setup guide** - Review all steps carefully
2. **Verify prerequisites** - Ensure correct versions are installed
3. **Check ports** - Ensure 3000 and 5000 are available
4. **Read error messages** - Console output often shows the issue
5. **Check file permissions** - Ensure proper read/write access
6. **Restart services** - Stop and restart both frontend and backend

**Still having issues?**

- 📧 Create an issue on GitHub
- 💬 Check existing issues for solutions
- 📖 Review the [README.md](README.md) for additional information

---

**🎉 Congratulations!**

You should now have a fully functional e-voting system running locally.

Happy coding! 🗳️✨
