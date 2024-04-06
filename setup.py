from setuptools import find_packages,setup
from typing import List

"""HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements"""

setup(
    name='restraurantratingprediction',
    version='0.0.1',
    author='vinay',
    author_email='vinayakavirat008@gmail.com',
    install_requires=["pandas","numpy","scikit-learn","matplotlib"],
    packages=find_packages(),
    install_requirs=["pandas","numpy","scikit-learn","matplotlib","seaborn","ipykernel"]
)
