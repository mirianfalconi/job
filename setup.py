from setuptools import setup

setup(name='FlaskApp',
      version='1.0',
      description='A basic Flask app with static files',
      author='Ryan Jarvinen',
      author_email='ryanj@redhat.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask>=0.10.1', 'CairoSVG>=1.0.19', 'Flask-WTF>=0.12', 'Flask-MySQL>=1.3',
                        'Flask-WeasyPrint>=0.5', 'FormEncode>=1.3.0', 'FormEncode-Jinja2>=0.1.2', 'Jinja2>=2.8',
                        'MarkupSafe>=0.23', 'Pyphen>=0.9.2', 'WTForms>=2.0.2', 'WeasyPrint>=0.24', 'Werkzeug>=0.10.4',
                        'cairocffi>=0.7.2', 'cffi>=1.3.1', 'click>=5.1', 'cssselect>=0.9.1', 'html5lib>=0.9999999',
                        'itsdangerous>=0.24', 'pycparser>=2.14', 'six>=1.10.0', 'tinycss>=0.3', 'lxml=3.5.0'],
      )