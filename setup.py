from distutils.core import setup

setup(
    name='Glider Database Alternative with Mongo NetCDF Subscriber',
    version='1.0',
    author='Michael Lindemuth',
    author_email='mlindemu@usf.edu',
    packages=['gdam_netcdf_subscriber'],
    scripts=[
        'scripts/gdam_netcdf_sub.py'
    ]
)
