# encoding: utf-8
from setuptools import setup, find_packages

import chargify


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


requirements = [
    'requests>=2.5.0,<3.0.0',
]


setup(
    name='chargify-python',
    version=chargify.__version__,
    long_description=readme,
    url='https://github.com/code-kitchen/chargify-python/',
    license=license,
    author='Ben Tappin',
    author_email='ben@codekitchen.io',
    install_requires=requirements,
    packages=find_packages(exclude=['test_*.py']),
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    )
)
