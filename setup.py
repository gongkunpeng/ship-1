# encoding: utf-8

from setuptools import setup, find_packages
import cli

# version
version = 0.12


# entry_points
entry_points = {
    'console_scripts':[
        'ship = cli.ship:cli'
    ]
}


setup(
    name='ship-cli',
    version=version,
    packages=find_packages(),
    url='https://github.com/neo1218/ship',
    license='MIT',
    author='neo1218',
    author_email='neo1218@yeah.net',
    description='python static site generator',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'click',
        'Flask',
        'Frozen-Flask',
        'Flask-Flatpages',
        'Flask-Wtf',
        'Flask-Script'
    ],
    entry_points=entry_points,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
