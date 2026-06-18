from huggingface_hub import snapshot_download

print("Downloading full model repository...")
# This pulls down every single block (json, vocabulary text, safetensors weights)
snapshot_download(
    repo_id="sentence-transformers/all-MiniLM-L6-v2", 
    local_dir="local_model",
    local_dir_use_symlinks=False
)
print("Download Complete! Check your 'local_model' folder.")