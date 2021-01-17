from setuptools import setup, find_packages

README = '{{cookiecutter.description}}'

requires = []
tests_require = [
        'pytest',
        'coverage'
        ]

setup(name='{{cookiecutter.name}}',
      version='0.0.1',
      description=README,
      long_description=README,
      package_dir={'': 'source'},
      classifiers=[
          "Programming Language :: Python",
      ],
      author='{{cookiecutter.author}}',
      author_email="{{cookiecutter.email}}",
      packages=find_packages('source'),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points={
          'console_scripts': [ '{{cookiecutter.name}} = {{cookiecutter.name}}.main:main' ]
      },
      )
