from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Other Audience',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.6'
]
 
setup(
  name='fpldata',
  version='0.0.2',
  description='Getting data out of FPL API made easier',
  long_description=open('README.md').read() ,
  long_description_content_type = 'text/markdown',
  url='https://github.com/Harsh1347/FPLDATA',  
  author='Harsh Gupta',
  author_email='harshapj2@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='FPL', 
  packages=find_packages(),
  install_requires=['requests','pandas'],
  
)