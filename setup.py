import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='youtube_lv',
    version='1.3.0',
    author="phillychi3",
    author_email="phillychi3@gmail.com",
    description="check youtuber live status",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phillychi3/youtube_lv",
    py_modules=["youtube","youtuber","status","live"],
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
 )