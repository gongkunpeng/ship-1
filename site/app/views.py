# coding: utf-8
"""
    views.py
    ````````
"""

from . import app
from . import pages
from flask import render_template, request
from .paginate import _Pagination


""" Views Config """
post_per_page = _num =  app.config.get('POST_PER_PAGE')
blog_title = app.config.get('BLOG_TITLE')
blog_url = app.config.get('BLOG_URL')
blog_desc = app.config.get('BLOG_DESC')
blog_keywords = app.config.get('BLOG_KEYWORDS')
github_url = app.config.get('GITHUB_URL')
""""""


""" API """
posts = [p for p in pages if 'date' in p.meta]
posts_sum = len(posts)
latests = sorted(posts, key=lambda p: p.meta['date'], reverse=True)
tags = [tag for tag in (p.meta.get('tag') for p in latests)]
archive = {}.fromkeys([str(p.meta.get('date'))[:-3] for p in latests]).keys()
""""""


@app.route('/')
def index():
    """
    index page
    -- latests(pagination)
    -- tags, archive, posts_sum
    """
    page = int(request.args.get('page') or 1)
    if isinstance(latests, list):
        _latests = _Pagination(latests, page, _num)  # paginate object
    return render_template(
        'index.html',
        latests=_latests, tags=tags,
        archive=archive, posts_sum=posts_sum,
        blog_url=blog_url, blog_title=blog_title,
        blog_desc=blog_desc, blog_keywords=blog_keywords,
        github_url=github_url)


@app.route('/<path:path>')
def post(path):
    post = pages.get_or_404(path)
    return render_template(
        'post.html', post=post,
        tags=tags, archive=archive)


@app.route('/archieve/<string:year>')
def archieve(year):
    posts = [p for p in pages if year in \
            str(p.meta.get('date')[-3])]
    return render_template(
        'archive.html', posts=posts,
        posts_sum=posts_sum, year=year)


@app.route('/tags/<string:tag>')
def tags(tag):
    posts = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tags.html',
        tag = tag,
        posts = posts,
        posts_sum = posts_sum)


# @app.route('/about')
# def about():
#     pass
