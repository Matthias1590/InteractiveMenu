from setuptools import setup


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="interactivemenu",
    version="1.0.0",
    description="An easy-to-use python package to create interactive menus in the terminal. ",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Matthias1590/InteractiveMenu",
    author="Matthias Wijnsma",
    author_email="matthiasx95@gmail.com",
    license="MIT",
    python_requires=">=3.6",
    packages=["interactivemenu"]
)
