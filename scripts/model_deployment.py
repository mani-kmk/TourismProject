import os
from huggingface_hub import HfApi

def deploy_model():
    # Define the repository and file paths
    model_repo_id = "maniKKrishnan/tourism-customer-prediction"
    model_filename = "best_model.pkl"

    # Get the token from the environment variable set in GitHub Actions
    token = os.environ.get("HF_TOKEN")

    if not token:
        print("Error: Hugging Face token not found. Please set the HF_TOKEN environment variable.")
        return

    # Define the path to the model file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    model_path = os.path.join(project_root, model_filename)

    if not os.path.exists(model_path):
        print(f"Error: Model file '{model_path}' not found.")
        return

    # Use the Hugging Face API to upload the file
    api = HfApi(token=token)

    print(f"Uploading model to {model_repo_id}...")
    api.upload_file(
        path_or_fileobj=model_path,
        path_in_repo=model_filename,
        repo_id=model_repo_id,
        repo_type="model",
    )
    print("Model deployment complete.")

if __name__ == "__main__":
    deploy_model()
