from setuptools import find_packages, setup

setup(
    name="CircleChatbot",
    version="0.0.1",
    author="maliktalha",
    author_email="muhammadtalhaawan801@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain_ai21','langchain-core','sentence_transformers','python-dotenv','flask']
)