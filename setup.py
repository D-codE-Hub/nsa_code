from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nsa_code/__init__.py
from nsa_code import __version__ as version

setup(
	name="nsa_code",
	version=version,
	description="App for Networking Solutions Australia Pty Ltd",
	author="Networking Solutions Australia Pty Ltd",
	author_email="shane.reglin@nsau.com.au",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
