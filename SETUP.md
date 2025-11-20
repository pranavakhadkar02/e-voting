# E-Voting System Setup Guide

Complete setup instructions for macOS and Windows 11 systems.

## Prerequisites

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

3. **Install Node.js**
   ```bash
   brew install node
   # Verify installation
   node --version
   npm --version
   ```

### Windows 11 Setup

1. **Install Python 3.8+**

   - Download from [python.org](https://www.python.org/downloads/)
   - ✅ Check "Add Python to PATH" during installation
   - Open Command Prompt and verify: `python --version`

2. **Install Node.js**

   - Download from [nodejs.org](https://nodejs.org/)
   - Run the installer
   - Open Command Prompt and verify: `node --version` and `npm --version`

3. **Install Git** (if not already installed)
   - Download from [git-scm.com](https://git-scm.com/)

## Project Setup

### Step 1: Clone/Download Project

If you have Git:

```bash
git clone <repository-url>
cd e-voting
```

Or download and extract the project files to a folder named `e-voting`.

### Step 2: Backend Setup

#### macOS

```bash
cd e-voting/backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
```

#### Windows 11

```cmd
cd e-voting\backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
copy .env.example .env
```

### Step 3: Configure Email (Optional)

Edit the `.env` file in the backend directory:

```env
# Gmail Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
```

**Gmail Setup:**

1. Go to Google Account settings
2. Enable 2-factor authentication
3. Generate an App Password
4. Use the App Password (not your regular password)

**Note:** The app works without email configuration, but OTP verification will be disabled.

### Step 4: Frontend Setup

#### Both macOS and Windows

```bash
cd e-voting/frontend

# Install dependencies
npm install
```

## Running the Application

### Start Backend Server

#### macOS

```bash
cd e-voting/backend
source venv/bin/activate
python app.py
```

#### Windows 11

```cmd
cd e-voting\backend
venv\Scripts\activate
python app.py
```

**Backend will run on:** http://localhost:5000

### Start Frontend Server

#### Both Systems

```bash
cd e-voting/frontend
npm start
```

**Frontend will run on:** http://localhost:3000

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

## Troubleshooting

### Common macOS Issues

**Command not found: python3**

```bash
# Try these alternatives
python --version
which python3
# If using Homebrew
brew install python
```

**Permission denied errors**

```bash
# Use --user flag
pip install --user -r requirements.txt
```

### Common Windows Issues

**'python' is not recognized**

- Reinstall Python with "Add to PATH" checked
- Or use full path: `C:\Python39\python.exe`

**Scripts execution policy error**

```cmd
# Run as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Port already in use**

```cmd
# Find and kill process using port 5000
netstat -ano | findstr :5000
taskkill /PID <process-id> /F
```

### Database Issues

**Database locked**

- Stop the backend server
- Delete `backend/evoting.db` file
- Restart the backend (database will be recreated)

**Missing database file**

- The database is created automatically on first run
- Make sure you're in the correct directory
- Check file permissions

### Email Issues

**Gmail authentication error**

- Ensure 2-factor authentication is enabled
- Use App Password, not regular password
- Check for typos in email settings

**OTP not received**

- Check spam folder
- Verify email address spelling
- Check backend console for error messages

### Network Issues

**Can't access from other devices**

- Backend: Change `app.run(debug=True, host='0.0.0.0', port=5000)`
- Frontend: Use `npm start -- --host 0.0.0.0`
- Ensure firewall allows connections

## Development Tips

### Hot Reload

- Frontend: Automatically reloads on file changes
- Backend: Restart manually or use Flask development mode

### Database Inspection

```bash
# Install SQLite browser (macOS)
brew install --cask db-browser-for-sqlite

# Open database file
# backend/evoting.db
```

### API Testing

Use tools like:

- **Postman** - GUI API client
- **curl** - Command line tool
- **Browser DevTools** - Network tab

### Code Editor Setup

- **VS Code** with Python and React extensions
- **PyCharm** for Python development
- **WebStorm** for React development

## Production Deployment

### Environment Variables

Set these in production:

```env
SECRET_KEY=your-production-secret-key
JWT_SECRET_KEY=your-production-jwt-secret
DATABASE_URL=your-production-database-url
MAIL_USERNAME=your-production-email
MAIL_PASSWORD=your-production-email-password
```

### Security Considerations

- Use strong, unique secret keys
- Enable HTTPS in production
- Use production database (PostgreSQL)
- Set up proper logging
- Configure rate limiting
- Regular security updates

---

## Getting Help

If you encounter issues:

1. Check this troubleshooting section
2. Verify all prerequisites are installed
3. Ensure ports 3000 and 5000 are available
4. Check console/terminal for error messages
5. Make sure both frontend and backend are running

**System Requirements:**

- **macOS**: 10.14+ (Mojave or later)
- **Windows**: Windows 10/11
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 1GB free space

Good luck with your e-voting system! 🗳️
