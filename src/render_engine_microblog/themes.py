from render_engine.utils.themes import Theme
from jinja2 import PackageLoader

microblog_theme = Theme(
    loader = PackageLoader('render_engine_microblog', 'templates'),
    plugins = {},
    filters = [],
)
