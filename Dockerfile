# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot script
COPY whisper.py .

# Expose port
EXPOSE 8080

# Run the bot
CMD ["python", "whisper.py"]
