# coding: utf-8
"""
    config.py
    `````````
"""


class Config(object):
    DEBUG = True
    FLATPAGES_AUTO_RELOAD = DEBUG
    FLATPAGES_EXTENSION = '.md'


class ExampleConfig(Config):
    # [site setting]
    site_name = "shipsite"
    site_url = "https://neo1218.github.io"
    site_desc = "a ship site"
    site_owner = "neo1218"

    # [article setting]
    article_type = FLATPAGES_EXTENSION = '.md'  # default is .md
    article_per_page = 10

    # [deploy on github/(git) pages]
    git_url = "https://github.com/neo1218"
    repo_name = "Test"
    brance = "gh-pages"
    FREEZER_BASE_URL = GIT_URL + "/" + REPO_NAME


class MyConfig(Config):
    # [site setting]
    site_name = ""
    site_url = ""
    site_desc = ""
    site_owner = ""

    # [article setting]
    article_type = FLATPAGES_EXTENSION = ""
    article_per_page = 10

    # [deploy on github/(git) pages]
    git_url = ""
    repo_name = ""
    brance = ""
    FREEZER_BASE_URL = GIT_URL + "/" + REPO_NAME


config = {
    'default': ExampleConfig
}
