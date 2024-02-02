from render_engine.blog import Blog
from render_engine.page import Page
from render_engine_markdown import MarkdownPageParser

from .themes import microblog_theme


class MicroBlogPost(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def _slug(self):
        return self.date.strftime("%Y%m%d%H%M")

    @property
    def _title(self):
        return ""


class MicroBlog(Blog):
    required_themes = [microblog_theme]
    Parser = MarkdownPageParser
    content_type = MicroBlogPost
    archive_template = "microblog/microblog.html"
    has_archive = True
