from setuptools import setup, find_packages

setup(
    name="PopModLib",
    version="0.1.0",
    description="Population modelling library",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,                
    package_data={"PopModLib": ["py.typed"]}, 
    install_requires=[
    ],
    python_requires=">=3.13",
    zip_safe=False,
)