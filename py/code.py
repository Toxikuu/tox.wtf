from jinja2 import Environment, FileSystemLoader
import os
import shutil
from vars import *


def render_code():
    """
    Template and render all pages in pages/code, using the base.html located
    there.
    """
    env = Environment(loader=FileSystemLoader("pages/code"))

    for f in generate_code_list():
        template = env.get_template(f)
        rendered = template.render(f=os.path.splitext(f)[0])

        outpath = os.path.join(target, f"code/{f}")
        outdir = os.path.dirname(outpath)

        os.makedirs(outdir, exist_ok=True)
        with open(outpath, "w") as f:
            f.write(rendered)


def render_code_index():
    env = Environment(loader=FileSystemLoader("pages/code"))
    template = env.get_template("index.html")

    code = [
        {"name": os.path.splitext(f)[0], "href": f}
        for f in generate_code_list()
    ]

    rendered = template.render(code=code)
    outpath = os.path.join(target, "code/index.html")
    os.makedirs(os.path.dirname(outpath), exist_ok=True)

    with open(outpath, "w") as f:
        f.write(rendered)


def generate_code_list():
    files = [ f for f in os.listdir(os.path.join(pages_dir, "code")) if f.endswith(".html") and not f in ignore ]
    files.sort(key=lambda f: os.path.getmtime(os.path.join(pages_dir, f"code/{f}")))
    return files
