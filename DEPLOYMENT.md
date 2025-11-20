# E-Voting System Deployment Guide

## Free Cloud Deployment Options

### Render (Full Stack) ⭐ **CURRENTLY DEPLOYED**

**🚨 IMMEDIATE ACTION REQUIRED for Mail Issues:**

If you're experiencing 502 errors and mail not sending:

1. **Go to Render Dashboard → Your Service → Environment**
2. **Add missing environment variable:**
   - Key: `MAIL_DEFAULT_SENDER`
   - Value: `your-email@gmail.com` (same as MAIL_USERNAME)
3. **Verify Gmail App Password:**
   - MAIL_PASSWORD must be 16-character App Password, not regular password
4. **Redeploy service** (Environment changes trigger automatic redeploy)
5. **Test**: Visit `https://your-service.onrender.com/api/health`

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

4. **Environment Variables** ⚠️ **CRITICAL FOR MAIL FUNCTIONALITY**

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
   MAIL_PASSWORD=your-gmail-app-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   ```

   **⚠️ IMPORTANT**: For Gmail, you MUST use an App Password, not your regular password:

   - Enable 2-Factor Authentication on Gmail
   - Generate App Password: Google Account → Security → 2-Step Verification → App passwords
   - Use the 16-character app password as `MAIL_PASSWORD`

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
   - Render: Apps sleep after 15 minutes of inactivity on free tier
   - Consider upgrading for production use with high traffic

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

#### Mail Not Sending & 502 Errors on Render 🚨

**Common Issues & Solutions:**

1. **Missing MAIL_DEFAULT_SENDER Environment Variable**

   - Go to Render Dashboard → Your Service → Environment
   - Add: `MAIL_DEFAULT_SENDER` = `your-email@gmail.com`
   - **This is often the cause of 502 errors**

2. **Gmail App Password Required**

   - Regular Gmail password won't work
   - Must use 16-character App Password
   - Enable 2FA first, then generate App Password

3. **Check Service Health**

   - Visit: `https://your-service.onrender.com/api/health`
   - Should show mail configuration status
   - Look for "mail": "configured" in response

4. **View Render Logs**

   - Go to Render Dashboard → Your Service → Logs
   - Look for mail-related errors
   - Check for "Error sending email" messages

5. **Render Free Tier SMTP Limitations**
   - Some free tiers may block SMTP
   - Consider upgrading to paid tier
   - Or use email service like SendGrid

**Quick Diagnostic Steps:**

```bash
# Test your service health
curl https://your-service.onrender.com/api/health

# Test registration (should send OTP email)
curl -X POST https://your-service.onrender.com/api/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

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

#### Other Common Issues on Render

- **502 Bad Gateway**: Usually caused by missing environment variables or SMTP timeouts

  - Check all environment variables are set correctly
  - Verify MAIL_DEFAULT_SENDER is configured
  - Check service logs for timeout errors

- **CORS errors**: Check that your frontend URL is allowed in CORS settings

  - Backend automatically allows all origins in development
  - For production, update CORS settings if needed

- **Database errors**: Verify DATABASE_URL is correctly set

  - Should be automatically set when PostgreSQL database is connected
  - Check connection in Render dashboard

- **Email not working**:

  - Verify Gmail App Password (not regular password)
  - Check MAIL_DEFAULT_SENDER environment variable
  - Test with `/api/health` endpoint
  - Consider using SendGrid for production

- **App sleeping**: Render free tier sleeps after 15 minutes of inactivity

  - First request after sleep may be slow
  - Consider upgrading for production use

- **Build failures**:
  - Check Python version matches `runtime.txt`
  - Verify all dependencies in `requirements.txt`
  - Check build logs in Render dashboard

### Custom Domain (Optional)

Render allows custom domains on free tiers:

- Add your domain in the Render dashboard
- Update DNS records as instructed
- SSL certificates are automatically provided
