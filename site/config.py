# coding: utf-8
"""
    config.py
    `````````

    ship-site user config

    :License :: MIT
    :Copyright @neo1218 2016
"""


class Config(object):
    DEBUG = True
    FLATPAGES_AUTO_RELOAD = DEBUG
    FLATPAGES_EXTENSION = '.md'


class ExampleConfig(Config):
    # [site setting]
    SITE_NAME = "shipsite"
    SITE_URL = "https://neo1218.github.io"
    SITE_DESC = "a ship site"
    SITE_OWNEr = "neo1218"

    # [article setting]
    ARTICLE_Type = FLATPAGES_EXTENSION = '.md'  # default is .md
    ARTICLE_PER_PAGE = 10

    # [owner info] 
    GITHUB_URL = "https://github.com/neo1218"
    WEIBO_URL = "http://www.weibo.com/5551886705/profile"
    TWITTER_URl = "https://twitter.com/neo1218substack"

    # [deploy on github/(git) pages]
    GIT_URL = "https://github.com/neo1218"
    REPO_NAME = "Test"
    BRANCH = "gh-pages"
    FREEZER_BASE_URL = GIT_URL + "/" + REPO_NAME


class MyConfig(Config):
    # [site setting]
    SITE_NAME = ""
    SITE_URL = ""
    SITE_DESC = ""
    SITE_OWNER = ""

    # [article setting]
    ARTICLE_TYPE = FLATPAGES_EXTENSION = ""
    ARTICLE_PER_PAGE = 10

    # [owner info]
    GITHUB_URL = ""
    WEIBO_URL = ""
    TWITTER_URl = ""

    # [deploy on github/(git) pages]
    GIT_URL = ""
    REPO_NAME = ""
    BRANCH = ""
    FREEZER_BASE_URL = GIT_URL + "/" + REPO_NAME


config = {
    'default': ExampleConfig
}
