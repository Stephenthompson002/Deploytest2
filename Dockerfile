FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install git and any required build tools
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy app files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the deployment script
CMD ["python", "deploy.py"]
