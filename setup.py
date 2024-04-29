# python3 -m venv venv
# source venv/bin/activate
# pip install -e .
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    description="My Custom Package",
    author="Your Name",
    packages=find_packages(where="src"),  # find_packagesでsrcディレクトリ以下のパッケージを検索
    package_dir={"": "src"},
    package_data={
        "get_images": ["*.py, component/*.py"],
        "mylib": ["*.py"]
    },
)
