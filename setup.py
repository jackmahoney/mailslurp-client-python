import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mailslurp-client",
    version="0.0.1",
    author="MailSlurp",
    author_email="jackmahoney212@gmail.com",
    description="Official MailSlurp client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mailslurp/mailslurp-client-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "mailslurp_sdk @ git+ssh://github.com/mailslurp/swagger-sdk-python@56730668bf94b9eff88d742bfeb6fd0f828b1ace#egg=mailslurp_sdk"
    ]
)
