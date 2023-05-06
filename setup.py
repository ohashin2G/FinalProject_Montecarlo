from setuptools import setup, find_packages

setup(
    name='Project_Package',
    version='1.0.0',
    url='https://github.com/ohashin2G/FinalProject_Montecarlo',
    author='Naomi Ohashi',
    author_email='ohashin2@gmail.com',
    description='Mote Carlo Simulator',
    packages=find_packages(),    
    install_requires=['click'],
)