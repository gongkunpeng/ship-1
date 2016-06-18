# coding: utf-8
"""
    config.py
    `````````
"""


class Config(object):
    DEBUG = True
    FLATPAGES_AUTO_RELOAD = DEBUG
    FLATPAGES_EXTENSION = '.md'


class LConfig(Config):
    POST_PER_PAGE = 10
    BLOG_TITLE = "L"
    BLOG_URL = "http://neo1218.github.io/l"
    BLOG_DESC = "python static site generator"
    BLOG_KEYWORDS = "python static generator"
    GITHUB_URL = "http://neo1218.github.io"


config = {
    'default': LConfig
}
