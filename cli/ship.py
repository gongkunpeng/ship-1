# coding: utf-8
"""
    ship::cli::ship.py
    ``````````````````

    ship commandline tool

    :License :: MIT
    :Copyright @neo1218 2016
"""

import platform
import click
import os
import shutil
import datetime
from functools import wraps

from operators import _mkdir_p, _touch_file, _copy_files
from templates import md, sails

import logging
from logging import StreamHandler, DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(DEBUG)
logger.addHandler(StreamHandler())


_platform = platform.platform().split('-')[0]
site_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def run_in_root(f):
    """
    make sure all the cli run under site root path
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        path = os.getcwd()
        _dot_site_path = os.path.join(path, '.site')
        if not os.path.isfile(_dot_site_path):
            logger.warning('''\033[31m{warning}\033[0m
                ==> please run the command under site root folder!''')
            exit(1)
        else:
            f(*args, **kwargs)
    return decorator


def warning_path_exist(path):
    """
    send warning msg if path exist
    """
    logger.warning('''\033[31m{Warning}\033[0m
                   ==> \033[32m%s\033[0m\n exist
                   ==> please change the project name,
                   ==> and try again !''' % path)


def start_init_info(path):
    """
    start init msg
    """
    if os.path.isdir(path):
        warning_path_exist(path)
        exit(1)
    else:
        logger.info('''\033[33m{Info}\033[0m\n
                    ==> start init your static site [on]
                    ==> \033[32m%s\033[0m\n''' % path)


def finish_init_info():
    logger.info('''\033[33m{Info}\033[0m\n
                ==> finish init your ship site''')


@click.group()
def cli():
    pass


@click.command()
@click.option('--dev', is_flag=True)
@click.argument('site_name')
def init(dev, site_name):
    site = os.path.join(site_path, 'site')
    dst = os.path.join(os.getcwd(), site_name)
    
    start_init_info(dst)
    _mkdir_p(dst)

    for site_dir, sub_dirs, filenames in os.walk(site):
        relative = site_dir.split(site)[1].lstrip(os.path.sep)
        dst_dir = os.path.join(dst, relative)

        _mkdir_p(dst_dir)

        for filename in filenames:
            site_file = os.path.join(site_dir, filename)
            dst_file = os.path.join(dst_dir, filename)

            shutil.copy(site_file, dst_file)

    if not dev:
        themes_path = os.path.join(dst, 'app/themes')
        os.chdir(dst)
        os.popen('git clone https://github.com/neo1218/ship-theme-cat.git app/themes/cat')
        os.popen('ship upgrade cat')

    finish_init_info()
    os.chdir(dst)
    os.popen('ship server')


@click.command()
@click.option('--port', default=5050)
@run_in_root
def server(port):
    logger.info("%s" % sails)
    os.popen("python2 manage.py runserver --port %d" % port)


@click.command()
@click.argument('file_name')
@run_in_root
def new(file_name):
    current_path = os.getcwd()
    file_path = os.path.join(current_path, 'app/pages', file_name+'.md')
    if os.path.exists(file_path):
        warning_path_exist(file_path)
    else:
        new_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        _touch_file(file_path, md % new_time)
        logger.info('''\033[33m{Info}\033[0m
                    ===> new a markdown file \033[34m%s\033[0m''' % file_path)


@click.command()
@run_in_root
def build():
    build_path = os.path.join(os.getcwd(), 'app/build')
    os.popen('python manage.py build')
    logger.info('''\033[33m{Info}\033[0m
                ===> static your site in \033[34m%s\033[0m''' % build_path)


@click.command()
@run_in_root
def upload():
    current_path = os.getcwd()
    root_path = current_path
    harbor_folder = os.path.join(root_path, '.harbor')
    build_folder = os.path.join(root_path, 'app/build')

    if not os.path.exists(harbor_folder):
        _mkdir_p(harbor_folder)
        os.chdir(harbor_folder)
        os.popen('git init')
        os.chdir(root_path)
        _copy_files(build_folder, harbor_folder)
        os.popen('python manage.py first_upload')
    else:
        os.chdir(root_path)
        _copy_files(build_folder, harbor_folder)
        os.popen('python manage.py other_upload')

    os.chdir(root_path)
    logger.info('deployment done!')


@click.command()
@click.argument('theme_name')
@run_in_root
def upgrade(theme_name):
    root_path = os.getcwd()
    templates_target_path = os.path.join(root_path, 'app/templates') 
    static_target_path = os.path.join(root_path, 'app/static')

    templates_path = os.path.join(root_path,
                                  'app/themes/%s/templates' % theme_name)
    static_path = os.path.join(root_path, 'app/themes/%s/static' % theme_name)

    if os.path.isdir(templates_target_path):
        shutil.rmtree(templates_target_path)
    if os.path.isdir(static_target_path):
        shutil.rmtree(static_target_path)
    shutil.copytree(templates_path, templates_target_path)
    shutil.copytree(static_path, static_target_path)

    logger.info('''\033[33m{info}\033[0m\n
                ==> upgrade theme to \033[33m{%s}\033[0m
                ''' % theme_name)


cli.add_command(init)
cli.add_command(server)
cli.add_command(build)
cli.add_command(new)
cli.add_command(upload)
cli.add_command(upgrade)
