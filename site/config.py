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
    GIT_URL = "https://github.com/neo1218"
    REPO_NAME = "shipdoc"
    BRANCH = "gh-pages"
    FREEZER_BASE_URL = GIT_URL+"/"+REPO_NAME


class MyConfig(Config):
    POST_PER_PAGE = 10
    BLOG_TITLE = ""
    BLOG_URL = ""
    BLOG_DESC = ""
    BLOG_KEYWORDS = ""

    # [deploy on github pages]
    GIT_URL = ""
    REPO_NAME = ""
    BRANCH = ""
    FREEZER_BASE_URL = GIT_URL + "/" + REPO_NAME


config = {
    'default': ShipConfig
}
