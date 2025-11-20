#!/usr/bin/env python3
"""
Mail Configuration Diagnostic Script
This script helps diagnose mail configuration issues in production
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_environment_variables():
    """Check if all required mail environment variables are set"""
    print("=== Checking Environment Variables ===")
    
    required_vars = [
        'MAIL_SERVER',
        'MAIL_PORT',
        'MAIL_USERNAME',
        'MAIL_PASSWORD',
        'MAIL_DEFAULT_SENDER'
    ]
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if value:
            # Hide password for security
            display_value = value if var != 'MAIL_PASSWORD' else '*' * len(value)
            print(f"✓ {var}: {display_value}")
        else:
            print(f"✗ {var}: NOT SET")
            missing_vars.append(var)
    
    if missing_vars:
        print(f"\n⚠️  Missing variables: {', '.join(missing_vars)}")
        return False
    else:
        print("\n✓ All mail environment variables are set")
        return True

def test_smtp_connection():
    """Test SMTP connection to mail server"""
    print("\n=== Testing SMTP Connection ===")
    
    mail_server = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    mail_port = int(os.getenv('MAIL_PORT', 587))
    mail_username = os.getenv('MAIL_USERNAME')
    mail_password = os.getenv('MAIL_PASSWORD')
    
    if not mail_username or not mail_password:
        print("✗ Cannot test SMTP - missing credentials")
        return False
    
    try:
        print(f"Connecting to {mail_server}:{mail_port}...")
        
        # Create SMTP connection
        server = smtplib.SMTP(mail_server, mail_port)
        server.starttls()  # Enable TLS
        print("✓ TLS connection established")
        
        # Login
        server.login(mail_username, mail_password)
        print("✓ Authentication successful")
        
        server.quit()
        print("✓ SMTP connection test passed")
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"✗ Authentication failed: {e}")
        print("  This usually means:")
        print("  - Wrong username/password")
        print("  - App password needed (for Gmail)")
        print("  - 2FA not properly configured")
        return False
        
    except smtplib.SMTPConnectError as e:
        print(f"✗ Connection failed: {e}")
        print("  Check if server and port are correct")
        return False
        
    except Exception as e:
        print(f"✗ SMTP test failed: {e}")
        return False

def send_test_email():
    """Send a test email"""
    print("\n=== Sending Test Email ===")
    
    mail_server = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    mail_port = int(os.getenv('MAIL_PORT', 587))
    mail_username = os.getenv('MAIL_USERNAME')
    mail_password = os.getenv('MAIL_PASSWORD')
    mail_sender = os.getenv('MAIL_DEFAULT_SENDER', mail_username)
    
    if not all([mail_username, mail_password]):
        print("✗ Cannot send test email - missing credentials")
        return False
    
    # Use sender's email for test
    test_recipient = mail_username
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = mail_sender
        msg['To'] = test_recipient
        msg['Subject'] = "E-Voting System - Mail Configuration Test"
        
        body = """
        This is a test email from your E-Voting System.
        
        If you received this email, your mail configuration is working correctly!
        
        Configuration details:
        - Mail Server: {mail_server}
        - Mail Port: {mail_port}
        - Sender: {mail_sender}
        
        Timestamp: {timestamp}
        """.format(
            mail_server=mail_server,
            mail_port=mail_port,
            mail_sender=mail_sender,
            timestamp=os.popen('date').read().strip()
        )
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(mail_server, mail_port)
        server.starttls()
        server.login(mail_username, mail_password)
        server.send_message(msg)
        server.quit()
        
        print(f"✓ Test email sent successfully to {test_recipient}")
        return True
        
    except Exception as e:
        print(f"✗ Failed to send test email: {e}")
        return False

def main():
    """Run all diagnostic tests"""
    print("E-Voting System - Mail Configuration Diagnostics")
    print("=" * 50)
    
    # Check environment variables
    env_ok = check_environment_variables()
    
    if not env_ok:
        print("\n❌ Environment variables not properly configured")
        print("Please set all required mail environment variables")
        return
    
    # Test SMTP connection
    smtp_ok = test_smtp_connection()
    
    if not smtp_ok:
        print("\n❌ SMTP connection failed")
        print("Please check your mail server configuration")
        return
    
    # Send test email
    test_ok = send_test_email()
    
    if test_ok:
        print("\n✅ All mail configuration tests passed!")
        print("Your mail configuration should work in production")
    else:
        print("\n❌ Test email failed")
        print("Mail configuration may have issues")

if __name__ == "__main__":
    main()