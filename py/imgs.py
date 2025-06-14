from jinja2 import Environment, FileSystemLoader
import os
import shutil
from vars import *


def render_imgs():
    """
    Template and render all pages in pages/imgs, using the base.html located
    there.
    """
    env = Environment(loader=FileSystemLoader("pages/imgs"))

    for img in generate_imgs_list():
        template = env.get_template(img)
        rendered = template.render(img=os.path.splitext(img)[0])

        outpath = os.path.join(target, f"imgs/{img}")
        outdir = os.path.dirname(outpath)

        os.makedirs(outdir, exist_ok=True)
        with open(outpath, "w") as f:
            f.write(rendered)


def render_imgs_index():
    env = Environment(loader=FileSystemLoader("pages/imgs"))
    template = env.get_template("index.html")

    imgs = [
        {"name": os.path.splitext(img)[0], "href": img}
        for img in generate_imgs_list()
    ]

    rendered = template.render(imgs=imgs)
    outpath = os.path.join(target, "imgs/index.html")
    os.makedirs(os.path.dirname(outpath), exist_ok=True)

    with open(outpath, "w") as f:
        f.write(rendered)


def generate_imgs_list():
    files = [ f for f in os.listdir(os.path.join(pages_dir, "imgs")) if f.endswith(".html") and not f in ignore ]
    files.sort(key=lambda f: os.path.getmtime(os.path.join(pages_dir, f"imgs/{f}")))
    return files
