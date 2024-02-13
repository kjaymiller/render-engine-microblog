from jinja2 import PackageLoader
from render_engine.themes import Theme

microblog_theme = Theme(
    loader=PackageLoader("render_engine_microblog", "templates"),
    plugins={},
    filters=[],
    prefix="microblog",
)
