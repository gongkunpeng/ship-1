# coding: utf-8
"""
    config.py
    `````````
"""


class Config(object):
    DEBUG = True
    FLATPAGES_AUTO_RELOAD = DEBUG
    FLATPAGES_EXTENSION = '.md'


class ShipConfig(Config):
    POST_PER_PAGE = 10
    BLOG_TITLE = "L"
    BLOG_URL = "http://neo1218.github.io/l"
    BLOG_DESC = "python static site generator"
    BLOG_KEYWORDS = "python static generator"

    # [deploy on github pages]
    FREEZER_BASE_URL = "https://neo1218.github.io/ship/"
    BRANCH = "gh-pages"


class MyConfig(Config):
    POST_PER_PAGE = 10
    BLOG_TITLE = ""
    BLOG_URL = ""
    BLOG_DESC = ""
    BLOG_KEYWORDS = ""

    # [deploy on github pages]
    FREEZER_BASE_URL = ""
    BRANCH = ""


config = {
    'default': ShipConfig
}
