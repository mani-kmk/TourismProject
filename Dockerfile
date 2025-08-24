# Use a slim Python base image
FROM python:3.9-slim

# Create a non-root user and switch to it immediately
RUN adduser --system --group user
USER user

# Set the working directory for the user and create necessary directories
WORKDIR /home/user/app
RUN mkdir -p /home/user/.cache/huggingface

# Set environment variables for Hugging Face cache and pip installation
ENV HF_HOME="/home/user/.cache/huggingface"
ENV PIP_TARGET="/home/user/app/packages"
ENV PYTHONPATH="$PIP_TARGET:$PYTHONPATH"
ENV PATH="$PIP_TARGET/bin:$PATH"

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY predict.py .

# Expose the port for the FastAPI application
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]