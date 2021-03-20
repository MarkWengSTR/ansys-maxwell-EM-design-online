import setuptools

install_requires = [
    "setuptools",
    "pywin32==227",
    "ramda==0.5.5",
    "six==1.13.0",
    "functional-pipeline==0.3.1",
    "ipdb==0.12.3",
    "Flask==1.1.2",
    "Flask-Cors==3.0.8",
    "pandas==1.0.1",
    "numpy==1.18.1",
    "requests==2.24.0",
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anmotordesign",
    version="0.1a",
    author="Mark Weng",
    author_email="bskin0330@gmail.com",
    description="Electrical Machines Design Automation by Ansys Maxwell Script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarkWengSTR/ansys-maxwell-EM-design-online",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    python_requires=">=3.6",
)
