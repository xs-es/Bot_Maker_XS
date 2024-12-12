import os

def create_project_structure():
    # Define the directory structure
    directories = [
        'models',
        'src',
        'src/utils',
        'configs',
        'logs'
    ]
    
    # Create directories
    for dir in directories:
        os.makedirs(dir, exist_ok=True)
        print(f"Created directory: {dir}")

    # Create necessary files
    files = {
        'src/main.py': '',
        'src/gui.py': '',
        'src/utils/model_manager.py': '',
        'src/utils/inference.py': '',
        'configs/config.yaml': '',
        'requirements.txt': ''
    }
    
    for file_path, content in files.items():
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_project_structure() 