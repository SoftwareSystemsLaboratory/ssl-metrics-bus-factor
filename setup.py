from setuptools import setup

from clime_bus_factor import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="clime-bus-factor",
    packages=["clime_bus_factor"],
    version=version.version(),
    description="CLIME - Bus Factor Metric",
    author="Software and Systems Laboratory - Loyola University Chicago",
    author_email="ssl-metrics@ssl.luc.edu",
    license="BSD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ssl.cs.luc.edu/projects/metricsDashboard",
    project_urls={
        "Bug Tracker": "https://github.com/SoftwareSystemsLaboratory/clime-bus-factor/issues",
        "GitHub Repository": "https://github.com/SoftwareSystemsLaboratory/clime-bus-factor",
    },
    keywords=[
        "bugzilla",
        "bus factor",
        "bus factor",
        "cloc",
        "commits",
        "commits",
        "delta lines of code",
        "engineering",
        "git",
        "git",
        "github",
        "github",
        "gitlab",
        "installable",
        "issue density",
        "issue density",
        "issue spoilage",
        "issues",
        "issues",
        "kloc",
        "lines of code",
        "longitudinal graphs",
        "loyola university chicago",
        "loyola",
        "luc",
        "metrics",
        "metrics",
        "mining",
        "productivity",
        "python",
        "repository mining",
        "repository",
        "simple",
        "sloccount",
        "software engineering",
        "software metrics",
        "software systems laboratory",
        "software",
        "ssl"
        "thousands of lines of code",
        "tool",
        "vcs",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.9",
    install_requires=[
        "matplotlib",
        "numpy",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "clime-git-bus-factor-compute = clime_bus_factor.main:main",
            "clime-git-bus-factor-graph = clime_bus_factor.graph:main",
        ]
    },
)
