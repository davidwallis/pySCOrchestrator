from distutils.core import setup

setup(
    name='pyOrchestrator',
    version='0.0.1',
    author='davidwallis',
    author_email='david@wallis2000.co.uk',
    packages=['pyHyperV'],
    url='https://github.com/davidwallis3101/pyOrchestrator',
    license='Apache License',
    description='A simple client for calling System Center Orchestator runbooks in python',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests >= 2.0.0",
        "requests_ntlm",
        "xmltodict"
    ],
)
