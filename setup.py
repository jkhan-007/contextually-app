from setuptools import setup

requirements = [
    "PyQt5 == 5.10.1",
    "gitpython",
    "tinydb",
    "requests",
    "requests-cache"
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-faulthandler',
    'pytest-mock'
]

import contextual

app_name = contextual.__appname__
version = contextual.__version__
description = contextual.__description__

setup(
    name=app_name,
    version=version,
    description= description,
    author="JK",
    author_email='info@bettercallbots.com',
    url='https://github.com/jkhan-007/contextually-app',
    packages=['contextual', 'contextual.images',
              'contextual.tests'],
    package_data={'contextual.images': ['*.png']},
    entry_points={
        'gui_scripts': [
            'context=contextual.application:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='contextual-app',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
