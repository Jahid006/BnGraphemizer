from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "TRIE-based tokenizer for Text Recognintion"
LONG_DESCRIPTION = "TRIE-based tokenizer for Text Recognintion"

# Setting up
setup(
    name="BnGraphemizer",
    version=VERSION,
    author="Mohammad Jahid",
    author_email="<mohammadjahid1504037@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(include=["BnGraphemizer", "BnGraphemizer.*"]),
    install_requires=[
        "marisa_trie==0.7.8",
        "normalizer @ git+https://github.com/csebuetnlp/normalizer@d80c3c4",
    ],
    keywords=["python", "Text Tokenizer"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ],
)
