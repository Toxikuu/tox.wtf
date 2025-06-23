from jinja2 import Environment, FileSystemLoader
import os
import shutil
from vars import *


def render_imgs():
    """
    Template and render all pages in pages/imgs
    """

    for f in generate_imgs_list():
        fh = f"imgs/{f}.html"
        template = env.get_template(fh)
        rendered = template.render(f=f)

        outpath = os.path.join(target, fh)
        outdir = os.path.dirname(outpath)

        os.makedirs(outdir, exist_ok=True)
        with open(outpath, "w") as f:
            f.write(rendered)


def render_imgs_index():
    template = env.get_template("imgs/index.html")

    imgs = [
        {"name": f, "href": f}
        for f in generate_imgs_list()
    ]

    rendered = template.render(imgs=imgs)
    outpath = os.path.join(target, "imgs/index.html")
    os.makedirs(os.path.dirname(outpath), exist_ok=True)

    with open(outpath, "w") as f:
        f.write(rendered)


def generate_imgs_list():
    files = [ f for f in os.listdir(os.path.join(pages_dir, "imgs")) if f.endswith(".html") and not f in ignore ]
    files.sort(key=lambda f: os.path.getmtime(os.path.join(pages_dir, f"imgs/{f}")))
    return [ os.path.splitext(f)[0] for f in files ]
