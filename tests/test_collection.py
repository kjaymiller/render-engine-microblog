from render_engine_microblog.collection import MicroBlogPost
import datetime

def test_microblog_post_title_is_empty(base_microblog_post):
    """Tests that the title of a MicroBlogPost is empty"""
    assert base_microblog_post._title == ""

def test_microblog_post_slug_is_timestamp(base_microblog_post):
    """tests that the slug of the microblog post is a timestamp"""
    assert base_microblog_post._slug == "201801010000"

def test_microblog_slug_checks_date_published_or_date(base_microblog_post):
    """Tests that the slug of the microblog post is based on the date_published
    attribute if it exists, otherwise it is based on the date attribute
    """

    class DatePublishedMicroBlogPost(MicroBlogPost):
        content = "Hello World"
        date_published = datetime.datetime(2018, 1, 1, 0,0,0).astimezone()

    assert base_microblog_post._slug == "201801010000"
    assert DatePublishedMicroBlogPost()._slug == "201801010000"