from dateutil import parser
from render_engine.blog import Blog, BlogPost
from render_engine.parsers.markdown import MarkdownPageParser

class MicroBlogPost(BlogPost):
    @property
    def _slug(self):
        base_date = parser.parse(self.date)
        return base_date.strftime("%Y%m%d%H%M")

    @property    
    def _title(self):
        return ""

class MicroBlog(Blog):
    template = "blog.html"
    PageParser = MarkdownPageParser
    content_type = MicroBlogPost
