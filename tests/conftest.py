import pytest
import datetime
from render_engine_microblog.collection import MicroBlogPost

@pytest.fixture(scope="session")
def base_microblog_post():
    class BaseMicroBlogPost(MicroBlogPost):
        content = "Hello World"
        date = datetime.datetime(2018, 1, 1, 0,0,0).astimezone()
    return BaseMicroBlogPost()