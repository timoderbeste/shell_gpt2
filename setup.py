from setuptools import setup
setup(
    name='shell-gpt2',
    version='0.1.3',
    description="A somewhat more advanced version of Shell GPT",
    author="Timo Wang",
    author_email="ntwang1994@gmail.com",
    packages=["."],
    entry_points={
        "console_scripts": [
            "sgpt2 = main:main"
        ],
    },
    install_requires=[
        "shell_gpt",
    ]
)