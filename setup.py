from setuptools import setup

setup(name='django-drift-chatwidget',
      version='0.1.2',
      description="Easily add Drift's chat widget to your Django apps.",
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      author='Lemuel Boyce',
      author_email='lemuelboyce@gmail.com',
      packages=['drift_chatwidget', 'drift_chatwidget.templatetags'],
      url='https://github.com/Driftt/django-drift-chatwidget',
      include_package_data=True,
      zip_safe=False,
      license='MIT',
      install_requires=[
          'django >= 1.8'
      ])
