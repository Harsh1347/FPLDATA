from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Other Audience',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='fpldata',
  version='0.0.1',
  description='A simple library to get data out of the FPL API',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/Harsh1347/FPLDATA',  
  author='Harsh Gupta',
  author_email='harshapj2@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='FPL', 
  packages=find_packages(),
  install_requires=['requests'] 
)