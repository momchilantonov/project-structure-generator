from setuptools import setup, find_packages

setup(
    name='project-structure-creator',
    version='0.1.0',
    packages=find_packages(where='src'),
    # package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[],
    entry_points={
    'console_scripts': [
        'project-creator=project_structure_creator.main:main',
    ]
    },
    author='Momchil Antonov ',
    author_email='eng.antonov@gmail.com',
    description='A utility for creating project structures from JSON configurations',
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
