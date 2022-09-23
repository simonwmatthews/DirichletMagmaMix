import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DirichletMagmaMix",
    version="1.00", # REMEMBER TO UPDATE __INIT__.PY
    author="Simon Matthews",
    author_email="simonm@hi.is",
    description=("A python library for modelling partial melt aggregation"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simonwmatthews/DirichletMagmaMix",
    packages=setuptools.find_packages(),
    install_requires=[
            'pandas>=1.3.5',
            'numpy>=1.21.5',
            'pyMelt>=2.0'
            ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
