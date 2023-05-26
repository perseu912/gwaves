from setuptools import setup
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='gwaves',
    version='0.0.3.1',
    url='https://github.com/perseu912/gwaves',
    license='MIT License',
    author='Reinan Br',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='kit tools dev works',
    description=u'Library for getting music in high quality from YouTube',
    packages=find_packages(),
    install_requires=['scipy','requests','pandas','bs4','h5py','matplotlib','numpy','soundfile','astropy','openpyxl','lxml'],)
