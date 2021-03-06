from setuptools import setup, find_packages

setup(
    name = "Radiocrepe",
    version = "0.0.1",
    author = "Pedro Ferreira",
    author_email = "ilzogoiby@gmail.com",
    description = ("An office jukebox"),
    license = "BSD",
    keywords = "radio play music",
    url = "http://github.com/pferreir",
    packages=find_packages(),
    long_description=open('README.md', 'r').read(),
    classifiers=[
    ],
    include_package_data=True,
    package_data={
        'radiocrepe': ['*.sql']
    },
    install_requires=['mutagen', 'Flask', 'python-magic'],
    entry_points={'console_scripts': "radiocrepe=radiocrepe.main:main"},
    dependency_links=[],
    zip_safe=False)
