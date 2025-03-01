from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name='project-structure-generator',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'project_structure_generator': ['../configs/project_config.json'],
    },
    entry_points={
        'console_scripts': [
            'project-generator=project_structure_generator.main:main',
        ]
    },
    author='Momchil Antonov',
    author_email='eng.antonov@gmail.com',
    description='A utility for generating project structures from JSON configurations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/momchilantonov/project-structure-generator.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
