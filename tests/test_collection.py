import pytest
from render_engine.collection import MicroBlog, MicroBlogPost

def test_microblog_post_title_is_empty:
    class MBP(MicroBlogPost):
        pass
        content = "Hello World"

    assert MBP().title == ""