#!/bin/bash
"""
Startup script for production deployment
Initializes database and starts the application
"""

echo "Starting E-Voting System..."

# Initialize database
echo "Initializing database..."
python init_db.py

# Check if database initialization was successful
if [ $? -eq 0 ]; then
    echo "Database initialization completed successfully"
    
    # Start the application
    echo "Starting application server..."
    exec gunicorn --bind 0.0.0.0:$PORT app:app
else
    echo "Database initialization failed!"
    exit 1
fi