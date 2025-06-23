from jinja2 import Environment, FileSystemLoader
import os
import shutil
from vars import *


def render_logs():
    """
    Template and render all pages in pages/logs
    """

    for f in generate_logs_list():
        fh = f"logs/{f}.html"
        template = env.get_template(fh)
        rendered = template.render(f=f)

        outpath = os.path.join(target, fh)
        outdir = os.path.dirname(outpath)

        os.makedirs(outdir, exist_ok=True)
        with open(outpath, "w") as f:
            f.write(rendered)


def render_logs_index():
    template = env.get_template("logs/index.html")

    logs = [
        {"name": f, "href": f, "time": round(os.path.getctime(f"pages/logs/{f}.html"))}
        for f in generate_logs_list()
    ]

    rendered = template.render(logs=logs)
    outpath = os.path.join(target, "logs/index.html")
    os.makedirs(os.path.dirname(outpath), exist_ok=True)

    with open(outpath, "w") as f:
        f.write(rendered)


def generate_logs_list():
    files = [ f for f in os.listdir(os.path.join(pages_dir, "logs")) if f.endswith(".html") and not f in ignore ]
    files.sort(key=lambda f: os.path.getmtime(os.path.join(pages_dir, f"logs/{f}")))
    return [ os.path.splitext(f)[0] for f in files ]
