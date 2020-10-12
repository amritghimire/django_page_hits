#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ 'Django~=3.1.2']

setup(
    author="Amrit Ghimire",
    author_email='mail@amritghimire.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A middleware which stores the records of page view counts",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='django_page_hits',
    name='django_page_hits',
    packages=find_packages(include=['django_page_hits', 'django_page_hits.*']),
    setup_requires=setup_requirements,
    test_suite='django_page_hits.tests',
    tests_require=test_requirements,
    url='https://github.com/amritghimire/django_page_hits',
    version='0.1.0',
    zip_safe=False,
)
