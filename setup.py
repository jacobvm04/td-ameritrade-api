import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="td-ameritrade-api",
    version="1.0.4",
    author="Jacob Van Meter",
    author_email="jacobvm04@gmail.com",
    description="A python wrapper for the TD ameritrade API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacobvm04/td-ameritrade-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests'
    ]
)
