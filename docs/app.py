"""
This is a simple app setup script created with `render-engine init`
"""

import os

from render_engine import (
    Page,
    Site,
)
from render_engine.parsers.markdown import MarkdownPageParser

app = Site()
app.output_path = "output"
app.template_path = "docs/templates"
app.static_paths.add("docs/static")

if os.getenv("production", "false").lower() not in ["0", "false", "f"]:
    SITE_URL = "https://kjaymiller.github.io/microblog" 
else:
    SITE_URL = "http://localhost:8000"

app.site_vars.update(
    {
        "SITE_TITLE": "Render Engine Microblog",
        "SITE_URL": SITE_URL,
        "OWNER": {
            "name": "Jay Miller",
            "email": "kjaymiller@gmail.com",
        },
        "NAVIGATION": [
            {
                "name": "Home",
                "url": SITE_URL,
            },
        ],
    }
)

markdown_extras = [
    "admonitions",
    "footnotes",
    "fenced-code-blocks",
    "header-ids",
    "mermaid",
]


@app.page
class Index(Page):
    content_path = "README.md"
    Parser = MarkdownPageParser
    template = "index.html"
    parser_extras = {"markdown_extras": markdown_extras}


if __name__ == "__main__":
    app.render()
