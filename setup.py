from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
name = 'mlproject',
version='0.0.1',
author='Gourav Singh',
description="A package for creating machine learning projects",
author_email='gouravsingh2480@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
# This is a list of all the dependencies that are required to run this project.

)