import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="utils", # unoriginal name is not a problem since this "package" is not meant for pypi
    version="0.1",
    author="Manuel A. Vázquez",
    author_email="manuavazquez@gmail.com",
    description="Utility functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manuvazquez/utils",
    packages=setuptools.find_packages(),
    install_requires=['h5py', 'pyyaml', 'numpy', 'matplotlib', 'scipy', 'nvidia-ml-py3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
