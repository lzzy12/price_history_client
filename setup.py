from setuptools import setup, find_packages

setup(
    name='price_history',
    packages=find_packages(include=['price_history']),
    version='0.1.3',
    description='A rest client for pricehistory.in',
    author='lzzy12',
    license='GPLv3',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    # tests_require=['pytest==4.4.1'],
)