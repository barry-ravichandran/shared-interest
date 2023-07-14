from setuptools import setup, find_packages

setup(name='shared_interest',
      version='0.1',
      description='Shared Interest evaluation for deep learning models.',
      url='https://github.com/mitvis/shared-interest',
      author='Angie Boggust',
      author_email='aboggust@mit.edu',
      license='MIT',
      packages=find_packages('shared_interest/'),
      package_dir={'': 'shared_interest/'},
      zip_safe=False)
