from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vies_validation/__init__.py
from vies_validation import __version__ as version

setup(
	name="vies_validation",
	version=version,
	description="Validate customers Tax ID vs EU VIES system",
	author="KAINOTOMO PH LTD",
	author_email="info@kainotomo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
