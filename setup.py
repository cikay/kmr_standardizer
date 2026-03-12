from setuptools import setup, find_packages

setup(
    name="kmr_standardizer",
    version="0.1.0",
    description="Kurdish Kurmanji text standardizer based on Rêbara Rastnivîsînê by Weqfa Mezopotamya",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Muzaffer Cikay",
    url="https://github.com/muzaffercky/kmr_standardizer",
    packages=find_packages(),
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Kurdish",
        "Topic :: Text Processing :: Linguistic",
    ],
)
