from setuptools import setup, find_packages

setup(
    name='parsecfi',
    version='0.1.0',
    description='Python SDK for the Parsec API',
    author='PARSEC FINANCE INC.',
    packages=[
        'parsecfi',
        'parsecfi.lib',
        'parsecfi.lib.endpoints_list'
    ],
    license='MIT',
    install_requires=[
        'requests',
        'pandas'
    ]
)