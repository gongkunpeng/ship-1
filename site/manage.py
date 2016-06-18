# coding: utf-8

"""
    manage.py
    ~~~~~~~~
"""

import os
import sys
from app import app, freezer
from flask_script import Manager


"""编码设置"""
# reload(sys) is evil :)
reload(sys)
sys.setdefaultencoding('utf-8')


manager = Manager(app)


def upload():
    git_url = app.config['FREEZER_BASE_URL']
    git_branch = app.config['BRANCH']
    if not git_url:
        raise
    else:
        harbor_folder = os.path.join(os.getcwd(), '.harbor')
        os.chdir(harbor_folder)
        os.popen('git add remote origin %s' % git_url)
        os.popen('git add .')
        os.popen('git commit -m "ship site update"')
        os.popen('git push origin %s' % git_branch)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    elif len(sys.argv) > 1 and sys.argv[1] == 'upload':
        upload()
    else:
        manager.run()
