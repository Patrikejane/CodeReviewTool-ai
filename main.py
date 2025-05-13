import os
from logging import root

from tools.file_reader import read_project_files
from tools.standard_parser import parse_standards
from tools.code_reviewer import review_code
from tools.html_reporter import generate_html_report

def main():
    project_path = "./sample_project"  # replace with real path
    standards_file = "standards.md"

    standards = parse_standards(standards_file)
    code_files = read_project_files(project_path)
    
    reviews = []
    for path, content in code_files.items():
        for file in project_path:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                if os.path.isfile(filepath):  # ✅ Ensure it's a file, not a folder
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()

                print(f"🔍 Reviewing {filepath}...")
                result = review_code(content, standards)

        result = review_code(content, standards)
        reviews.append({"filename": path, "result": result})

    generate_html_report(reviews)
    print("Code review completed. Report saved as code_review_report.html")

if __name__ == "__main__":
    main()
