# coding: utf-8

"""
    manage.py
    ~~~~~~~~
"""

import sys
from app import app, freezer
from flask_script import Manager


"""编码设置"""
# reload(sys) is evil :)
reload(sys)
sys.setdefaultencoding('utf-8')


manager = Manager(app)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        manager.run()
