"""
Setup for carla_ad_agent
"""
from distutils.core import setup
from catkin_pkg.python3_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['carla_ad_agent'],
    package_dir={'': 'src'}
)

setup(**d)
