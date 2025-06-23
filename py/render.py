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


if __name__ == "__main__":
    # Some setup
    os.makedirs(target, exist_ok=True)
    shutil.copytree("static", f"target/s", dirs_exist_ok=True)

    # Rendering
    render_root()
    pkgs.render_pkgs_index()
    pkgs.render_pkgs()
    logs.render_logs_index()
    logs.render_logs()
    imgs.render_imgs_index()
    imgs.render_imgs()
    code.render_code_index()
    code.render_code()
    read.render()
    _self.render()
    print(f"Site rendered to {target}")
