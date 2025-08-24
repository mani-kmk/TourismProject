# Use a slim Python base image
FROM python:3.9-slim

# Set the working directory for the application
WORKDIR /app

# Copy the requirements file and install dependencies as root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download the model file during the build to a known location
RUN python -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='maniKKrishnan/tourism-customer-prediction', filename='model_lgbm.pkl')"

# Copy the application code
COPY predict.py .

# Expose the port for the FastAPI application
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]