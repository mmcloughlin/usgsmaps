from setuptools import setup
import re

pkg_init_file = open('usgsmaps/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", pkg_init_file))

def readme():
    return open('./README.rst').read()

setup(name='usgsmaps',
      version=metadata['version'],
      description='Fetch top maps from USGS',
      long_description=readme(),
      url='https://github.com/mmcloughlin/usgsmaps',
      author='Michael McLoughlin',
      author_email='mmcloughlin@gmail.com',
      license='MIT',
      packages=['usgsmaps'],
      install_requires=[
          'requests',
          'pyproj',
          ],
      )
