from jinja2 import Environment, FileSystemLoader
import os
import shutil
from vars import *


def render_logs():
    """
    Template and render all pages in pages/logs, using the base.html located
    there.
    """
    env = Environment(loader=FileSystemLoader("pages/logs"))

    for log in generate_logs_list():
        template = env.get_template(log)
        rendered = template.render(log=os.path.splitext(log)[0])

        outpath = os.path.join(target, f"logs/{log}")
        outdir = os.path.dirname(outpath)

        os.makedirs(outdir, exist_ok=True)
        with open(outpath, "w") as f:
            f.write(rendered)


def render_logs_index():
    env = Environment(loader=FileSystemLoader("pages/logs"))
    # print(os.listdir("."))

    template = env.get_template("index.html")

    logs = [
        {"name": os.path.splitext(log)[0], "time": round(os.path.getctime(f"pages/logs/{log}")), "href": log}
        for log in generate_logs_list()
    ]

    rendered = template.render(logs=logs)
    outpath = os.path.join(target, "logs/index.html")
    os.makedirs(os.path.dirname(outpath), exist_ok=True)

    with open(outpath, "w") as f:
        f.write(rendered)


def generate_logs_list():
    files = [ f for f in os.listdir(os.path.join(pages_dir, "logs")) if f.endswith(".html") and not f in ignore ]
    files.sort(key=lambda f: os.path.getmtime(os.path.join(pages_dir, f"logs/{f}")))
    return files
