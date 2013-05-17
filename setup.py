from setuptools import setup

setup(
    name='wiktionary',
    version='0.0.2',
    author='Christopher Brown',
    author_email='chrisbrown@utexas.edu',
    packages=['wiktionary'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'wikitools',
        'lxml',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
