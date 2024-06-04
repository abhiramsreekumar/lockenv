import setuptools


setuptools.setup(
    name="lockenv",
    version="1.0",
    scripts=["lockenv"],
    author="Abhiram Sreekumar",
    author_email="ferncrypter@randomsasi.in",
    description="A utility to encrypt and decrypt env variables to safely store them in code repositories",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abhiramsreekumar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
