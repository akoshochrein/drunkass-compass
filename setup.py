from setuptools import setup, find_packages

setup(
    name='drunkass-compass',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'googlemaps',
        'keyring'
    ],
    entry_points='''
        [console_scripts]
        drunkass-compass=drunkass_compass.drunkass_compass:main
    ''',
)
