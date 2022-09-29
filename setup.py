from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='SE HW LUA to Python',
    version='1.0',
    description='SE HW 2 3 4 5',
    long_description=readme,
    author='SE Group 10',
    url='https://github.com/boscosylvester-john/se_hw_LuaToPython',
    packages=find_packages(exclude=('tests','docs'))
)