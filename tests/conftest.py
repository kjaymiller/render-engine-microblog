import pytest
import datetime
from render_engine import Site
from render_engine_microblog import MicroBlog
from render_engine_microblog.collection import MicroBlogPost

@pytest.fixture(scope="module")
def microblog_post():
    class MBP(MicroBlogPost):
        content = "Hello World"
        date = datetime.datetime(2018, 1, 1, 0, 0, 0)

    return MBP()


@pytest.fixture(scope="module")
def microblog_collection(tmp_path_factory):
    mb_content_path = tmp_path_factory.getbasetemp().joinpath("microblog_collection")
    tmp_path_factory.getbasetemp().joinpath("microblog_collection").mkdir()
    tmp_path_factory.getbasetemp().joinpath("microblog_collection/201801010000.md").write_text(
        """---\ndate: 2018-01-01T00:00:00Z\n---\nHello World""",
    )
    class MicroBlogCollection(MicroBlog):
        content_path = mb_content_path

    return MicroBlogCollection()

@pytest.fixture(scope="session")
def microblog_site(tmp_path_factory):
    
    mb_output_path = tmp_path_factory.getbasetemp() / "microblog_output"
    mb_collection_path = tmp_path_factory.getbasetemp() / "microblog_site_collection"

    mb_collection_path.mkdir()
    mb_collection_path.joinpath("201801010000.md").write_text(
        """---\ndate: 2018-01-01T00:00:00Z\n---\nHello World""",
    )

    class MicroBlogSite(Site):
        output_path = mb_output_path

    microblog_site = MicroBlogSite()
    @microblog_site.collection
    class TestMicroBlog(MicroBlog):
        content_path = mb_collection_path

    microblog_site.render()
    return microblog_site
