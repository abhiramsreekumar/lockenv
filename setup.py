import setuptools


setuptools.setup(
    name="lockenv",
    version="1.1",
    scripts=["lockenv"],
    author="Abhiram Sreekumar",
    author_email="ferncrypter@randomsasi.in",
    description="A CICD friendly pip package for encrypting env's to be stored safely in code repositories, No more hassle in handiling env's in cloud environments",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abhiramsreekumar/lockenv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
