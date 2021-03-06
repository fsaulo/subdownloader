#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2018 SubDownloader Developers - See COPYING - GPLv3

import gettext
from pathlib import Path
from setuptools import find_packages, setup

from sphinx.setup_command import BuildDoc

gettext.NullTranslations().install()

import subdownloader.project
project_path = Path(__file__).absolute().parent


def read(filename):
    return (project_path / filename).read_text()

install_requires = [
    'argparse >= 1.3.0',
    'argcomplete >= 1.7.0',
    'langdetect >= 1.0.7',
    'pymediainfo >= 2.1.6',
    'PyQt5 >= 5.0.0',
]

setup_requires = [
    'sphinx-argparse >= 0.2.1',
    'docutils >= 0.14',
]

tests_requires = [
    'pytest >= 3.4',
]

setup(
    name=subdownloader.project.PROJECT_TITLE,
    version=subdownloader.project.PROJECT_VERSION_FULL_STR,
    author=subdownloader.project.PROJECT_AUTHOR_COLLECTIVE,
    author_email=subdownloader.project.PROJECT_MAINTAINER_MAIL,
    maintainer_email=subdownloader.project.PROJECT_MAINTAINER_MAIL,
    description=subdownloader.project.get_description(),
    keywords=('download', 'upload', 'automatic', 'subtitle', 'movie', 'video', 'film', 'search'),
    license='GPL3',
    packages=find_packages(exclude=('tests', 'tests.*', )),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url=subdownloader.project.WEBSITE_MAIN,
    download_url=subdownloader.project.WEBSITE_RELEASES,
    project_urls={
        'Source Code': subdownloader.project.WEBSITE_MAIN,
        'Bug Tracker': subdownloader.project.WEBSITE_ISSUES,
        'Translations': subdownloader.project.WEBSITE_TRANSLATE,
    },
    classifiers=[
        'Topic :: Multimedia',
        'Topic :: Utilities',
        'Environment :: Console',
        'Environment :: X11 Applications :: Qt',
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_requires,
    entry_points={
        'console_scripts': [
            'subdownloader = subdownloader.client.__main__:main'
        ],
    },
    include_package_data=True,
    cmdclass={
        'build_sphinx': BuildDoc,
    },
    command_options={
        'build_sphinx': {
            'project': ('setup.py', subdownloader.project.PROJECT_TITLE, ),
            'version': ('setup.py', subdownloader.project.PROJECT_VERSION_STR, ),
            'release': ('setup.py', subdownloader.project.PROJECT_VERSION_FULL_STR, ),
            'builder': ('setup.py', 'man', ),
            'source_dir': ('setup.py', 'doc', ),
        },
    },
)
