# coding: utf-8

import click
import sys
import os
import shutil
import datetime
from functools import wraps

from os.path import dirname, abspath
from operators import _mkdir_p, _touch_file
from templates import sails, md

import logging
from logging import StreamHandler, DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(DEBUG)
logger.addHandler(StreamHandler())


_site_name = 'site'
site_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def run_in_root(f):
    """
    make sure all the cli run under site root path
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        path = os.getcwd()
        if path.split('/')[-1] != _site_name:
            logger.warning( '''\033[31m{warning}\033[0m
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
        logger.info('''\033[33m{Info}\033[0m
                    ==> start init your static site [on]
                    ==> \033[32m%s\033[0m\n''' % path)


def finish_init_info():
    logger.info('''\033[33m{Info}\033[0m \
                ==> finish init your flask project''')


@click.group()
def cli():
    pass


@click.command()
@click.argument('site_name')
def init(site_name):
    # os.environ['_SITE_NAME'] = site_name
    global _site_name
    _site_name = site_name
    site = os.path.join(site_path, 'site')
    dst = os.path.join(os.getcwd(), _site_name)

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
            logger.info("\033[34m<New>\033[0m: %s" % dst_file)

    finish_init_info()
    os.chdir(dst)
    os.popen('ship server')


@click.command()
@click.option('--port', default=5050)
@run_in_root
def server(port):
    logger.info("%s" % sails)

    os.popen("python manage.py runserver --port %d" % port)


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
    # now, the problem is how 2 use frozen-flask to generate static site

    build_path = os.path.join(os.getcwd(), 'app/build')
    if build_path:
        os.popen('sudo rm -rf %s' % build_path)
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

    for dirpath, sub_dirs, filenames in os.walk(build_folder):
        relative = dirpath.split(build_folder)[1].lstrip(os.path.sep)
        harbor_dir = os.path.join(harbor_folder, relative)

        _mkdir_p(harbor_dir)

        for filename in filenames:
            build_file = os.path.join(dirpath, filename)
            harbor_file = os.path.join(harbor_dir, filename)

            shutil.copy(build_file, harbor_file)

    os.popen('python manage.py upload')
    os.chdir(root_path)
    logger.info('deployment done!')


cli.add_command(init)
cli.add_command(server)
cli.add_command(build)
cli.add_command(new)
cli.add_command(upload)
# cli.add_command(status)  # 查看状态, 目前共有多少篇博客, archieve, tags... theme... giturl...
