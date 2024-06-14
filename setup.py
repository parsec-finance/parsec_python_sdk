from setuptools import setup, find_packages

setup(
    name='parsecfi',
    version='0.1.5',
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

# to release increment version and run
#
# python setup.py sdist bdist_wheel
# twine upload dist/*
#
# python setup.py sdist bdist_wheel && twine upload dist/*