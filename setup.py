try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'python streaming log ',
    'author': 'Yu Ruidong',
    'url': 'git@github.com:yuruidong/python-streaming.git',
    'author_email': 'yrd_1989@126.com',
    'version': '0.1',
    'install_requires': ['nose', 'kafka-python'],
    'packages': ['pystreaming'],
    'script': [],
    'name': 'python-streaming'
}

setup(**config)
