from render_engine.blog import Blog
from render_engine.page import Page
from render_engine.parsers.markdown import MarkdownPageParser

class MicroBlogPost(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = self._content

    @property
    def _slug(self):
        for attr in ["date_published", "date"]:
            if getattr(self, attr, None):
                return getattr(self, attr).strftime("%Y%m%d%H%M")

    @property    
    def _title(self):
        return ""

class MicroBlog(Blog):
    template = "blog.html"
    PageParser = MarkdownPageParser
    content_type = MicroBlogPost
