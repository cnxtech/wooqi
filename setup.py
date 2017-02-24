"""
pip package setup
"""

from setuptools import setup, find_packages

# For development purposes, install it with pip install -user -e
# or python setup.py develop
setup(
    version="0.2",
    name="wooqi",
    description="Pytest plugin allowing to parametrize all the test sequence thanks to a config file",
    packages=find_packages(),
    entry_points={
        'pytest11': [
            'wooqi = wooqi.plugin'], 'console_scripts': ['wooqi = wooqi.__main__:main']},
    include_package_data=True,
    install_requires=["pytest>=3.0.5", "pytest-rerunfailures==1.0.1",
                      "pytest-timeout==1.2.0", "pytest-spec==1.1.0"],
    setup_requires=["pytest-runner"],
    test_require=["pytest"],
)
