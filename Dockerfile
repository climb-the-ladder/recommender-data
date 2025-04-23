FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy data and code separately for better organization
COPY raw/ /app/raw/
COPY processed/ /app/processed/

# Ensure the processed directory exists
RUN mkdir -p /app/processed/output

# Set the working directory to the root of the project
WORKDIR /app

# Set the default command
CMD ["python", "processed/preprocess_data.py"] 
