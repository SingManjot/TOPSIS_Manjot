import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis",
    version="1.0.0",
    author="Manjot Singh Kandhari",
    author_email="smanjot444@gmail.com",
    description="Calculates Topsis Score and Rank them accordingly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/SingManjot/TOPSIS_Manjot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["TOPSIS_Manjot"],
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=TOPSIS_Manjot.topsis:main",
        ]
    },
)