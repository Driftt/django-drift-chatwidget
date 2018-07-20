import os
from setuptools import setup


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('drift_chatwidget')

setup(name='django-drift-chatwidget',
      version='0.0.1',
      description="Easily add Drift's chat widget to your Django apps.",
      long_description=open('README.md').read(),
      author='Lemuel Boyce',
      author_email='lemuelboyce@gmail.com',
      packages=["drift_chatwidget"],
      package_data={'': extra_files},
      url='https://github.com/rhymiz/django-drift-chatwidget',
      include_package_data=True,
      zip_safe=False,
      license='MIT',
      install_requires=[
          'django >= 1.8'
      ])