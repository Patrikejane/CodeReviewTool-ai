from jinja2 import Environment, FileSystemLoader

def generate_html_report(reviews):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")
    html_content = template.render(reviews=reviews)
    with open("code_review_report.html", "w", encoding="utf-8") as f:
        f.write(html_content)