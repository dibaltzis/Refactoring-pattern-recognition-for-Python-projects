import os
import shutil
import subprocess
from concurrent.futures import ProcessPoolExecutor
import src.config as config
"""
Need to run at the same directory as the src folder

Refactoring-recognition-for-python
├── Results/
├── Documentation/
├── src/
├── run_for_all_the_projects.py    <------
├── requirements.txt 
└── README.md
"""


def list_subfolders(folder_path):
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    return subfolders

def execute_subprocess(subfolder):
    try:
        if shutil.which("python"):
            python_command = "python"
        elif shutil.which("python3"):
            python_command = "python3"
        subprocess.run([python_command, "src/main.py", f"{subfolder}"], check=True)    
        #subprocess.run(["python3", "src/main.py", f"{subfolder}"], check=True)
        return f"Success for subfolder: {subfolder}"
    except subprocess.CalledProcessError as e:
        return f"Error running 'src/main.py' for subfolder {subfolder}: {e}"

if __name__ == "__main__":
    folder_path = config.PROJECT_FOLDER_PATH

    subfolders = list_subfolders(folder_path)
    
    # Specify the number of CPU cores
    num_cores = os.cpu_count()

    with ProcessPoolExecutor(max_workers=num_cores) as executor:
        results = executor.map(execute_subprocess, subfolders)
        
    for result in results:
        print(result)

