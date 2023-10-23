from dateutil import parser
from render_engine.page import Page
from render_engine.blog import Blog
from render_engine.parsers.markdown import MarkdownPageParser
from .themes import microblog_theme

class MicroBlogPost(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = self._content

    @property
    def _slug(self):
        return self.date.strftime("%Y%m%d%H%M")

    @property    
    def _title(self):
        return ""


class MicroBlog(Blog):
    required_themes = (microblog_theme)
    PageParser = MarkdownPageParser
    content_type = MicroBlogPost
    archive_template = "microblog.html"
    has_archive = True
