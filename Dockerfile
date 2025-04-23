FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create directory structure if it doesn't exist
RUN mkdir -p processed

# Set the default command
CMD ["python", "processed/preprocess_data.py"] 
