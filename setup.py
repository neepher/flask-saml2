# -*- coding: utf-8 -*-
from setuptools import setup
import saml2idp


with open('README.rst') as readme:
    description = readme.read()


with open('HISTORY.rst') as history:
    changelog = history.read()


setup(
    name='django-saml-idp',
    version=saml2idp.__version__,
    author='Gabriel de Forest, Sebastian Vetter',
    author_email='sebastian@mobify.com',
    description='SAML 2.0 IdP for Django',
    long_description='\n\n'.join([description, changelog]),
    install_requires=[
        'Django>=1.11',
        'ak-M2Crypto==0.24.0',
        'defusedxml>=0.5.0',
        'signxml>=2.4.0',
        'lxml>=3.8.0',
    ],
    license='MIT',
    packages=['saml2idp'],
    url='http://github.com/deforestg/dj-saml-idp',
    zip_safe=False,
    include_package_data=True,
)
