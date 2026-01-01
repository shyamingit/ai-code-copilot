import os

SUPPORTED_EXTENSIONS = {".py", ".js", ".ts", ".java", ".cpp", ".c", ".md"}

def scan_codebase(root_dir: str):
    files = []
    for root, _, filenames in os.walk(root_dir):
        for file in filenames:
            if os.path.splitext(file)[1] in SUPPORTED_EXTENSIONS:
                files.append(os.path.join(root, file))
    return files
