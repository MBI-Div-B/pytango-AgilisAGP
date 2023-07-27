from setuptools import setup, find_packages

setup(
    name="tangods_agilisagp",
    version="0.0.1",
    description="AgilisAGP Tango Device Server",
    author="Daniel Schick",
    author_email="dschick@mbi-berlin.de",
    python_requires=">=3.6",
    entry_points={"console_scripts": ["AgilisAGP = tangods_agilisagp:main"]},
    license="MIT",
    packages=["tangods_agilisagp"],
    install_requires=["pytango", "pyserial"],
    url="https://github.com/MBI-Div-b/pytango-AgilisAGP",
    keywords=[
        "tango device",
        "tango",
        "pytango",
        "agilisagp",
    ],
)
