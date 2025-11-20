FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create instance directory
RUN mkdir -p instance

# Make init_db.py executable
RUN chmod +x init_db.py

# Expose port
EXPOSE $PORT

# Make startup script executable
RUN chmod +x start.sh

# Run startup script
CMD ["./start.sh"]