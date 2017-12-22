from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open('requirements-test.txt','r') as f:
    test_requirements = f.read().splitlines()

setup(
    name = 'projectname',
    version = '0.1.0',
    description = """one line description""",
    author = "full name",
    author_email = "fulln@alleninstitute.org",
    url = 'https://github.com/AllenInstitute/projectname',
    packages = find_packages(),
    include_package_data=True,
    install_requires = requirements,
    entry_points={
          'console_scripts': [
              'projectname = projectname.__main__:main'
        ]
    },
    setup_requires=['pytest-runner'],
    tests_require = test_requirements
)
