try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An HTML table parser',
    'author': 'Ben Schmeckpeper',
    'url': 'https://github.com/bschmeck/tabler',
    'download_url': '',
    'author_email': 'ben.schmeckpeper@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['tabler'],
    'scripts': [],
    'name': 'tabler'
}

setup(**config)
