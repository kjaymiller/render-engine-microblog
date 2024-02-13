from gazpacho import Soup


def test_microblog_collection_has_div(microblog_site):
    p = microblog_site.output_path.joinpath("testmicroblog.html").read_text()
    soup = Soup(p)
    posts = soup.find("div", {"class": "microblog-post"})
    assert posts
