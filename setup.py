from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will returns the list of requirements
    '''
    Hypen_E_dot="-e ."
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]
        
        if Hypen_E_dot in requirements:
            requirements.remove(Hypen_E_dot)
    return requirements





setup(
    name='MLPROJECT_1',
    version='0.0.0.1',
    author='ANILKUMAR',
    author_email='rayapati.anil99@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))