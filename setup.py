from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='SPyObject',
    version='0.1.1',
    packages=['spyobject'],
    url='https://github.com/Phillyclause89/SPyObject',
    license='Apache License 2.0',
    author='Philip "Phillyclause89" Alexander-Lees',
    author_email='palexan127@gmail.com',
    description='A debugging tool for analysing Python objects',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
    ],
)
