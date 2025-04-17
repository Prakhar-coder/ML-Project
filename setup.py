from setuptools import setup,find_packages
from typing import List


#Declaring variables for setup functions
PROJECT_NAME="housing_predictor"
VERSION="0.0.1"
AUTHOR="Prakhar Gupta"
DESCRIPTION="Machine Learning Project"
PACKAGES=find_packages()
REQUIREMENR_FILE_NAME="requirements.txt"


def get_requirements_list():
    """
    Description:  This function is going to return list of requirement
    mention in requirements.txt file

    return: This function is going to return a list which contain name
    of libraries mention in requirements.txt file 
    
    """
    with open("requirements.txt") as requirement_file:
        return [
            req.strip() for req in requirement_file.readlines()
            if req.strip() and not req.startswith("-e")
        ]


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)