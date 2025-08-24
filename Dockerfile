# Use a slim Python base image
FROM python:3.9-slim

# Install the missing libgomp.so.1 dependency
RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model and application code
COPY predict.py .
COPY model_lgbm.pkl .

# Expose the port for the FastAPI application
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]

# The above code is for your Dockerfile.
