import os
import shutil
from vars import *

import pkgs
import logs
import imgs
import code
import read
import _self


def render_root():
    template = env.get_template("index.html")
    rendered = template.render()

    outpath = os.path.join(target, "index.html")
    with open(outpath, "w") as f:
        f.write(rendered)

def render_error_pages():
    for f in os.listdir("pages/err"):
        template = env.get_template(f"err/{f}")
        rendered = template.render()

        outpath = os.path.join(target, f)
        with open(outpath, "w") as f:
            f.write(rendered)


if __name__ == "__main__":
    # Some setup
    os.makedirs(target, exist_ok=True)
    shutil.copytree("static", f"target/s", dirs_exist_ok=True)

    # Render special pages
    render_root()
    render_error_pages()

    # Render normal pages
    pkgs.render()
    logs.render()
    imgs.render()
    code.render()
    read.render()
    _self.render()
    print(f"Site rendered to {target}")
