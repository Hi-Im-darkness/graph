from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

with open('README.rst', 'r') as f:
    license = f.read()

setup(
    name='graph',
    version='0.1',
    author='Hi Im darkness',
    author_email='nghthach98@gmail.com',
    description='A sample Python project',
    long_description=readme,
    license=license,
    packages=['graph'],
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': [
            'graph=graph.interface:cli',
        ],
    },
)
