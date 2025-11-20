# E-Voting System Deployment Guide

## Free Cloud Deployment Options

### Option 1: Railway (Recommended for Backend) + Vercel (Frontend)

#### Backend Deployment on Railway

1. **Sign up at [Railway](https://railway.app/)**

   - Connect your GitHub account

2. **Create a new project**

   - Click "New Project" → "Deploy from GitHub repo"
   - Select your e-voting repository
   - Choose the `backend` folder as the root directory

3. **Configure Environment Variables**
   Go to your project settings and add these environment variables:

   ```
   SECRET_KEY=your-very-secure-secret-key-here-make-it-long-and-random
   JWT_SECRET_KEY=your-jwt-secret-key-here-also-long-and-random
   FLASK_ENV=production
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-gmail-app-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   ```

4. **Add Database**

   - In Railway dashboard, click "New" → "Database" → "PostgreSQL"
   - Railway will automatically set the `DATABASE_URL` environment variable

5. **Deploy**
   - Railway will automatically deploy when you push to your main branch
   - Your backend will be available at `https://your-app-name.railway.app`

#### Frontend Deployment on Vercel

1. **Sign up at [Vercel](https://vercel.com/)**

   - Connect your GitHub account

2. **Create a new project**

   - Click "New Project"
   - Import your e-voting repository
   - Set root directory to `frontend`

3. **Configure Environment Variables**
   In project settings, add:

   ```
   REACT_APP_API_URL=https://your-backend-app.railway.app/api
   ```

4. **Deploy**
   - Vercel will automatically build and deploy
   - Your frontend will be available at `https://your-app-name.vercel.app`

### Option 2: Render (Full Stack) ⭐ **CURRENTLY DEPLOYED**

#### Backend on Render

1. **Sign up at [Render](https://render.com/)**

2. **Create Web Service**

   - Connect your GitHub repository
   - Select the backend folder
   - Use these settings:
     - Runtime: Python 3
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `python init_db.py && gunicorn app:app`

3. **Add PostgreSQL Database**

   - Create a new PostgreSQL database in Render
   - Copy the database URL to your web service environment variables

4. **Environment Variables**
   ```
   DATABASE_URL=(automatically set by Render when you connect the database)
   SECRET_KEY=your-secret-key
   JWT_SECRET_KEY=your-jwt-secret
   FLASK_ENV=production
   ADMIN_EMAIL=admin@yourdomain.com
   ADMIN_PASSWORD=your-secure-admin-password
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   ```

#### Frontend on Render

1. **Create Static Site**

   - Root directory: `frontend`
   - Build command: `npm run build`
   - Publish directory: `build`

2. **Environment Variables**
   ```
   REACT_APP_API_URL=https://your-backend-service.onrender.com/api
   ```

### Email Configuration (Gmail)

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
   - Use this password in `MAIL_PASSWORD` environment variable

### Important Notes

1. **CORS Configuration**: The backend is already configured to handle CORS for cross-origin requests.

2. **Database Initialization**: The app will automatically create tables and a default admin user on first run.

3. **Default Admin Credentials**:

   - Email: `admin@evoting.com`
   - Password: `admin123`
   - **Change these immediately after first login!**

4. **Environment Variables**: Never commit actual environment variables to your repository. Use the deployment platform's environment variable settings.

5. **Free Tier Limitations**:
   - Railway: 512MB RAM, $5/month credit (usually enough for small apps)
   - Render: Apps sleep after 15 minutes of inactivity on free tier
   - Vercel: Unlimited static deployments

### Recent Database Fix (November 2025)

**Issue Resolved**: "relation 'user' does not exist" error in production

**Solution Applied**: Added automatic database table creation during app startup. If you're seeing database errors, simply:

1. **Push the latest code** to trigger a redeploy on Render
2. **Wait for deployment** - tables will be created automatically
3. **Test login** with admin credentials

**Admin Credentials** (change after first login):

- Email: `admin@evoting.com` (or your `ADMIN_EMAIL` env var)
- Password: `admin123` (or your `ADMIN_PASSWORD` env var)

### Post-Deployment Checklist

1. ✅ Backend is accessible and returns JSON responses
2. ✅ Database connection is working (tables created automatically)
3. ✅ Frontend can communicate with backend API
4. ✅ Email functionality is working
5. ✅ Admin can log in and manage the system
6. ✅ Regular users can register and vote

### Troubleshooting

#### Database Issues on Render

If you encounter "relation 'user' does not exist" errors:

1. **Automatic Fix (Recommended)**: The latest code includes automatic database initialization

   - Simply redeploy your service on Render
   - Database tables will be created automatically on startup

2. **Manual Fix via Render Console**:

   - Go to your Render service dashboard
   - Click "Shell" to open web console
   - Run: `python init_db.py`

3. **Verify Database Connection**:
   - Ensure your PostgreSQL database is connected to your web service
   - Check that `DATABASE_URL` environment variable is set automatically

#### Other Common Issues

- **CORS errors**: Check that your frontend URL is allowed in CORS settings
- **Database errors**: Verify DATABASE_URL is correctly set
- **Email not working**: Check Gmail app password and SMTP settings
- **App sleeping**: Free tiers often sleep - consider upgrading for production use

### Custom Domain (Optional)

Both Railway and Vercel allow custom domains on free tiers:

- Add your domain in the platform's dashboard
- Update DNS records as instructed
- SSL certificates are automatically provided
