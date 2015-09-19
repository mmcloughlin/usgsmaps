from setuptools import setup
import re

pkg_init_file = open('topo/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", pkg_init_file))

def readme():
    return open('./README.rst').read()

setup(name='topo',
      version=metadata['version'],
      description='Fetch topo maps from USGS',
      long_description=readme(),
      url='https://github.com/mmcloughlin/topo',
      author='Michael McLoughlin',
      author_email='mmcloughlin@gmail.com',
      license='MIT',
      packages=['topo'],
      install_requires=[
          'requests',
          'pyproj',
          ],
      )
