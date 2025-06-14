from jinja2 import Environment, FileSystemLoader
import os
import shutil
from vars import *


def render_pkgs():
    """
    Template and render all pages in pages/pkgs, using the base.html located
    there.
    """
    env = Environment(loader=FileSystemLoader("pages/pkgs"))

    for pkg in generate_pkgs_list():
        template = env.get_template(pkg)
        rendered = template.render(pkg=os.path.splitext(pkg)[0])

        outpath = os.path.join(target, f"pkgs/{pkg}")
        outdir = os.path.dirname(outpath)

        os.makedirs(outdir, exist_ok=True)
        with open(outpath, "w") as f:
            f.write(rendered)


def generate_pkgs_list():
    files = [ f for f in os.listdir(os.path.join(pages_dir, "pkgs")) if f.endswith(".html") and not f in ignore ]
    files.sort()
    return files


def render_pkgs_index():
    env = Environment(loader=FileSystemLoader("pages/pkgs"))
    template = env.get_template("index.html")

    pkgs = [
        {"name": os.path.splitext(pkg)[0], "href": pkg}
        for pkg in generate_pkgs_list()
    ]

    rendered = template.render(pkgs=pkgs)
    outpath = os.path.join(target, "pkgs/index.html")
    os.makedirs(os.path.dirname(outpath), exist_ok=True)

    with open(outpath, "w") as f:
        f.write(rendered)
