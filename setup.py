import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='restapi3',
    version='0.0.1',
    author="imaging8896",
    author_email="imaging8896@gmail.com",
    description="Formatted APIs presentation for testing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imaging8896/restapi3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['setuptools', 'requests']
)