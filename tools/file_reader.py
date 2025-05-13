import os

def read_project_files(directory):
    code_files = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".py", ".js", ".ts", ".java", ".cs")):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    code_files[os.path.relpath(os.path.join(root, file), directory)] = f.read()
    return code_files