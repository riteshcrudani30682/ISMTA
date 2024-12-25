from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="indian_stock_analysis",
    version="1.0.0",
    author="Ritesh",
    author_email="your.email@example.com",
    description="A comprehensive Indian stock market analysis tool with technical indicators and sector analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/indian_stock_analysis",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements + ["click>=8.0.0"],
    entry_points={
        "console_scripts": [
            "indian-stock-analysis=indian_stock_analysis.cli:cli",
        ],
    },
)
