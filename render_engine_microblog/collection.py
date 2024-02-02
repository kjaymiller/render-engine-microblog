from render_engine.blog import Blog
from render_engine.page import Page
from render_engine_markdown import MarkdownPageParser

from .themes import microblog_theme


class MicroBlogPost(Page):
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
    template = "microblog/microblog_post.html"
    archive_template = "microblog/microblog.html"
    has_archive = True
