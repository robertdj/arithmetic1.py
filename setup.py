from setuptools import setup, find_packages

setup(
    name="arithmetic1",
    version="0.0.1",
    description="Simple arithmetic",
    author="Robert Dahl Jacobsen",
    package_dir={"": "src"},
    packages=find_packages("src"),
    license='MIT',
    tests_require=['pytest', "pytest-cov"],
    python_requires=">=3.7, <4"
)

