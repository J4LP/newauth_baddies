"""
NewAuth Baddies
===============

Show your alliance/corporations members that are not in NewAuth
"""
from setuptools import setup

setup(
    name='NewAuth Baddies',
    version='0.0.1',
    author='@adrien-f',
    author_email='vadrin_hegirin@j4lp.com',
    description='A plugin to show corporations members not in NewAuth',
    long_description=__doc__,
    packages=['newauth_baddies'],
    package_data={
            'newauth_baddies': ['templates/*.html']
    },
    zip_safe=True,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Classy',
    ]
)
