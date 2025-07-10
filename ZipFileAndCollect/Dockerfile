FROM python:3.10-slim

# Install Tkinter and other dependencies
RUN apt-get update && \
    apt-get install -y python3-tk && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your script (change this if needed)
CMD ["python", "run.py"]
