from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_requirement(file_path:str) -> list[str]:
    '''
    this fuction will return the list of requirements

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '')for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
    name = 'MLProject',
    version = '0.0.1',
    author = 'Aaron R',
    author_email ='aaronrijal43@gmail.com',
    packages=find_packages(),
    install_requires= get_requirement('requirement.txt')
)