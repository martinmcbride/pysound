from setuptools import setup, find_packages
 
setup(name='pysound',
      version='0.0',
      url='https://github.com/martinmcbride/pysound',
      license='MIT',
      author='Martin McBride',
      author_email='mcbride.martin@gmail.com',
      description='Sound synthesiser',
      packages=find_packages(exclude=['examples']),
      long_description=open('README.md').read(),
      setup_requires=[])
