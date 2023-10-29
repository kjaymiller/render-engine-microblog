from gazpacho import Soup

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


def test_microblog_archive_uses_microblog_theme(microblog_site):
    assert microblog_site.route_list["testmicroblog"].archive_template == "microblog.html"



def test_microblog_collection_has_div(microblog_site):
    p=microblog_site.output_path.joinpath("testmicroblog.html").read_text()
    soup = Soup(p)
    posts = soup.find("div", {"class": "microblog-post"})
    assert posts
