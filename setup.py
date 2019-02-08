from setuptools import setup


# Dynamically retrieve the information
MATHSOLVE = __import__('mathsolve')
VERSION = MATHSOLVE.__version__
AUTHOR = MATHSOLVE.__author__
AUTHOR_EMAIL = MATHSOLVE.__email__
URL = MATHSOLVE.__url__

with open("README.md", "r") as f:
    long_description = f.read()

setup (
    name='mathsolve',
    version=VERSION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description='Decode natural language to solve mathemathical calculations',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["mathsolve"],
    package_dir={'mathsolve':'mathsolve'},
    license='MIT',
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Text Processing :: General',
            'Topic :: Text Processing :: Linguistic',
            'Programming Language :: Python',
    ],
)
