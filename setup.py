from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
 
setup(name='pysound',
      version='0.0',
      url='https://github.com/martinmcbride/pysound',
      license='MIT',
      author='Martin McBride',
      author_email='mcbride.martin@gmail.com',
      description='Sound and music synthesiser',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages(exclude=['examples']),
      long_description=open('README.md').read(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
      setup_requires=[])
