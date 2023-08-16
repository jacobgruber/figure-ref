from os.path import abspath, dirname, join, normpath

import setuptools

setuptools.setup(
    # Basic package information:
    name='figure_ref',
    version='0.0.1',
    packages=['pelican.plugins.figure_ref'],
    package_dir={"": "."},


    # Packaging options:
    include_package_data=True,

    # Package dependencies:
    install_requires=['pelican>=4.8', 'bs4'],

)
