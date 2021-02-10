import setuptools
with open("lol", "r") as lo:
    long_description = lo.read()

setuptools.setup(
     name='youtube_lv',  
     version='0.0.1',
     author="phillychi3",
     author_email="phillychi3@gmail.com",
     description="check youtuber live status",
     long_description=long_description,
     url="https://github.com/phillychi3/youtube_live_status",
     py_modules=["youtube","youtuber","status","live"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ],
 )