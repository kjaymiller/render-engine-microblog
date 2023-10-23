import pytest
from render_engine_microblog.collection import MicroBlog, MicroBlogPost
from render_engine.site import Site
import datetime

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


def test_microblog_post_title_is_empty(microblog_post):
    """Tests that the title of a MicroBlogPost is empty"""

    assert microblog_post._title == ""

def test_microblog_post_slug_is_timestamp(microblog_post):

    assert microblog_post._slug == "201801010000"

def test_microblog_post_content_is_content(microblog_collection):
    page = list(microblog_collection)[0]
    assert page._slug == "201801010000"
    assert "<p>Hello World</p>" in page.content

def test_microblog_site_page(microblog_site):
    assert microblog_site.output_path.exists()
    assert "201801010000.html" in [x.name for x in microblog_site.output_path.iterdir()]
    page = microblog_site.output_path.joinpath("201801010000.html")
    assert "<p>Hello World</p>" in page.read_text()


def test_microblog_site_archive(microblog_site):
    archive = list(microblog_site.route_list['testmicroblog'].archives)[0]
    archive_template = archive.template
    assert  archive_template == "microblog.html"

    template = microblog_site.engine.get_template(archive_template)
    page = archive.pages[0]
    assert "<p>Hello World</p>" in page.content

    
    list(microblog_site.route_list['testmicroblog'].archives)[0].template == "microblog.html"
    page_output = microblog_site.output_path.joinpath("testmicroblog.html")
    assert "Untitled Site | TestMicroBlog"
    assert "<p>Hello World</p>" in page_output.read_text()


def test_microblog_site_loads_theme(microblog_site):
    print(microblog_site.engine.list_templates())
    assert "microblog.html" in microblog_site.engine.list_templates()