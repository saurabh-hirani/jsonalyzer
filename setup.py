from setuptools import setup, find_packages
setup(
  name='jsonalyzer',
  license='MIT',
  version='0.0.1',
  url='https://github.com/saurabh-hirani/jsonalyzer',
  description=('Because one life is too short to write boilerplate json again and again'),
  author='Saurabh Hirani',
  author_email='saurabh.hirani@gmail.com',
  packages=find_packages(),
  install_requires=[
    'click',
    'imp',
    'importlib',
    'simplejson'
  ],
  entry_points = {
    'console_scripts': [
      'jsonalyzer = jsonalyzer.cmdline:jsonalyzer',
    ]
  }
)
