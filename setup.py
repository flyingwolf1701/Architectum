"""
Setup script for Architectum Blueprint Generator.
"""

from setuptools import setup, find_packages

setup(
    name="arch_blueprint_generator",
    version="0.1.0",
    description="Generate structured JSON blueprints of codebases for consumption by AI agents and visualization tools",
    author="Architectum Team",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "hypothesis>=6.0.0",
        ],
    },
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "arch-blueprint=arch_blueprint_generator.cli:cli",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
