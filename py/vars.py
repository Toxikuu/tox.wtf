pages_dir = "pages"
target = "target"
ignore = ["index.html", "base.html", "macros.html"]

from jinja2 import Environment, FileSystemLoader, StrictUndefined
env = Environment(loader=FileSystemLoader("pages"), undefined=StrictUndefined)
