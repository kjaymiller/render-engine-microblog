import pytest
from render_engine_microblog.collection import MicroBlog, MicroBlogPost

def test_microblog_post_title_is_empty():
    """Tests that the title of a MicroBlogPost is empty"""
    class MBP(MicroBlogPost):
        content = "Hello World"
        date = "2018-01-01 00:00:00"

    assert MBP().title == ""

def test_microblog_post_slug_is_timestamp():
    class MBP(MicroBlogPost):
        content = "Hello World"
        date = "2018-01-01 00:00:00"

    assert MBP().slug == "201801010000"