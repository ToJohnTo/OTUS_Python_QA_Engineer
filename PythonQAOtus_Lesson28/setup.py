import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-tokarev-test",
    platforms="linux",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ToJohnTo",
    packages=["Test_REST_API_1", "Test_REST_API_2", "Test_REST_API_3", "Test_REST_API_4"],
    keywords='sample setuptools development',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=["requests==2.23.0", "pytest==5.4.1", "jsonschema==3.2.0", "mitmproxy==5.1.1"]
)

