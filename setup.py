from setuptools import setup, find_packages

def get_requirements(filepath):
    requirements=[]
    with open(filepath) as file_obj:
        requirements=[line.replace("\n","") for line in file_obj]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
            

setup(
    name='mlproject',
    version='0.0.1',
    author='Sanket Sinha',
    packages=find_packages(), # Automatically finds packages
    author_email="sinhasanket160@gmail.com",
    install_requires=get_requirements('requirements.txt')
)
