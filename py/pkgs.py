from jinja2 import Environment, FileSystemLoader
import os
import shutil
from vars import *


def render():
    file_list = generate_file_list()
    render_index(file_list)
    render_files(file_list)


def render_files(file_list):
    """
    Template and render all pages in pages/pkgs
    """

    for f in file_list:
        fh = f"pkgs/{f}.html"
        template = env.get_template(fh)
        rendered = template.render(f=f)

        outpath = os.path.join(target, fh)
        outdir = os.path.dirname(outpath)

        os.makedirs(outdir, exist_ok=True)
        with open(outpath, "w") as f:
            f.write(rendered)


def render_index(file_list):
    template = env.get_template("pkgs/index.html")

    pkgs = [
        {"name": f, "href": f}
        for f in file_list
    ]

    rendered = template.render(pkgs=pkgs)
    outpath = os.path.join(target, "pkgs/index.html")
    os.makedirs(os.path.dirname(outpath), exist_ok=True)

    with open(outpath, "w") as f:
        f.write(rendered)


def generate_file_list():
    files = [ f for f in os.listdir(os.path.join(pages_dir, "pkgs")) if f.endswith(".html") and not f in ignore ]
    files.sort()
    return [ os.path.splitext(f)[0] for f in files ]
