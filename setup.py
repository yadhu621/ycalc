from setuptools import setup, find_packages

long_description = 'Package to calculate simple and compound interest' 

setup( 
    name='ycalc',
    version='1.1.0',
    author='yadhu',
    author_email='yadhu621@gmail.com',
    url='https://github.com/yadhu621/ycalc',
    description='Simple and Compound interest calculator',
    long_description= long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['simple interest', 'calculator', 'compound interest'],
    zip_safe=False
)
