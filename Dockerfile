# Use a slim Python base image
FROM python:3.9-slim

# Create a non-root user and create necessary directories
RUN adduser --system --group user
RUN mkdir /home/user/app
RUN chown user:user /home/user/app

# Set the working directory for the user
WORKDIR /home/user/app
USER user

# Set environment variable for Hugging Face cache and create the directory
ENV HF_HOME="/home/user/.cache/huggingface"
RUN mkdir -p /home/user/.cache/huggingface

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY predict.py .

# Expose the port for the FastAPI application
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]