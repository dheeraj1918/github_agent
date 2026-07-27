import io
import os
import zipfile
import requests
# from transformers import pipeline

def analyze_github_repository(github_repo_url, branch_name="main", model_name="Qwen/Qwen2.5-Coder-7B-Instruct"):
    """
    Downloads a public GitHub repository, extracts code across all directories,
    and analyzes it using a Hugging Face LLM pipeline.
    """
    # 1. Convert standard repo URL to the direct ZIP archive download URL
    # Clean trailing slashes if present
    base_url = github_repo_url.rstrip("/")
    repo_zip_url = f"{base_url}/archive/refs/heads/{branch_name}.zip"
    
    # 2. Setup safe headers to prevent GitHub from blocking the automated request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"Connecting to GitHub: {repo_zip_url}...")
    response = requests.get(repo_zip_url, headers=headers)

    # 3. Verify GitHub actually returned the file successfully
    if response.status_code != 200:
        print(f"\n[ERROR] GitHub returned status code {response.status_code}.")
        if response.status_code == 404:
            print("Action item: Check if the repository URL or the branch name ('main' vs 'master') is correct.")
        elif response.status_code == 403:
            print("Action item: Access denied. The repository might be private or restricted.")
        return

    # 4. Safely extract files from the downloaded byte stream
    try:
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        print("Success: Repository ZIP file successfully loaded into memory.")
    except zipfile.BadZipFile:
        print("\n[ERROR] The downloaded payload is not a valid ZIP file.")
        print("GitHub response text preview:")
        print(response.text[:300])  # Show HTML error page context
        return

    # 5. Loop through all folders and consolidate code contents
    combined_code_text = ""
    allowed_extensions = (".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".cpp", ".h", ".cs", ".go", ".rs", ".html", ".css", ".md", ".json")
    ignored_folders = ("node_modules", "venv", ".git", "__pycache__", "dist", "build")

    print("Parsing files inside folders...")
    for file_path in zip_file.namelist():
        # Check if file resides inside an ignored directory layer
        if any(folder in file_path for folder in ignored_folders):
            continue
            
        # Filter for text-based code extensions to avoid bloating memory with binary assets
        if file_path.endswith(allowed_extensions):
            with zip_file.open(file_path) as file:
                try:
                    content = file.read().decode("utf-8")
                    # Append file structural marker so the model retains awareness of directory layout
                    combined_code_text += f"\n\n--- FILE PATH: {file_path} ---\n{content}"
                    print(combined_code_text)
                except UnicodeDecodeError:
                    # Skip files containing unreadable binary data encodings
                    continue

    if not combined_code_text.strip():
        print("[WARNING] No compatible text or code files found in the specified repository branch.")
        return

    # 6. Initialize Hugging Face pipeline for analysis
    # print(f"Loading Hugging Face model '{model_name}' (this might take a few moments)...")
    # Adjust device_map="auto" to use GPU if hardware acceleration is configured locally
    # analyzer = pipeline("text-generation", model=model_name, device_map="auto")

    # # 7. Construct contextual prompt and generate output
    # prompt = f"Analyze this complete repository structure and explain the key files and execution flow:\n{combined_code_text}"
    
    # print("Analyzing code base context...")
    # # max_new_tokens sets output size limits; adjust based on model context size boundaries
    # output = analyzer(prompt, max_new_tokens=800, clean_up_tokenization_spaces=True)
    
    # print("\n=== MODEL ANALYSIS RESULTS ===")
    # print(output[0]['generated_text'])

# Execution entry point
if __name__ == "__main__":
    # Target Repository Configuration
    TARGET_REPO = "https://github.com/dheeraj1918/Full-Stack-Firebase-User-Portfolio-System" 
    TARGET_BRANCH = "main"  # Change to "master" if working with an older codebase layout
    
    # analyze_github_repository(TARGET_REPO, branch_name=TARGET_BRANCH)
