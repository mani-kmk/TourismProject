# Use a slim Python base image
FROM python:3.9-slim

# Create a non-root user and necessary directories
RUN adduser --system --group user
RUN mkdir -p /home/user/app
RUN chown -R user:user /home/user

# Set the working directory and switch to the non-root user
WORKDIR /home/user/app
USER user

# Set environment variables for Hugging Face cache and pip installation
ENV HF_HOME="/home/user/.cache/huggingface"
ENV PIP_TARGET="/home/user/app/packages"
ENV PYTHONPATH="$PIP_TARGET:$PYTHONPATH"

# Create the directories for pip and cache
RUN mkdir -p /home/user/.cache/huggingface
RUN mkdir -p /home/user/app/packages

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY predict.py .

# Expose the port for the FastAPI application
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]