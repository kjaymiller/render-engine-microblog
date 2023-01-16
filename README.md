# Render Engine Microblog Parser

This is a parser To create a microblog using Render Engine. This is based on the [`Blog` Custom Collection](https://github.com/kjaymiller/render_engine/blob/main/src/render_engine/blog.py).

This follows the guidance used by [Micro.blog](https://micro.blog) which is to be a post with no title. Slugs by default are the slugified datetime string in `YYYYMMDDHHMMSS` format.

This will create an RSS feed that you can use to syndicate your microblog posts to other services.

Your content is expected to use renderi engine's `MarkdownPageParser` which is markdown with frontmatter. A `date` field is the only required metadata for the page object.

```
---
date: 2023-01-01 12:00:00
---

Hello **World**! 
```

## Installation

Install using pypi. If you haven't already, install [`render-engine`](https://pypi.org/project/render-engine/)

```bash
pip install render-engine render-engine-microblog
```

## Usage

### Import the parser and collection

In your render_engine config file import the `MicroBlog` collection class.

```python

from render_engine import Site
from render_engine_microblog import MicroBlog
```

### Create a collection for your site

Create your collection like you would a blog. You will need to pass a `content_path`.

```python
site = Site()

@site.collection
class MicroBlog(MicroBlog):
    content_path = "content/microblog"
```
