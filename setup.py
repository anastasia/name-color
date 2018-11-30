import os
from setuptools import setup
from setuptools.command.install import install
from subprocess import call


class Install(install):
    def run(self):
        install.run(self)
        call(['pip', 'install', '-r', 'requirements.txt'])


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname + '.md')).read()


setup(
    name="namecolor",
    version="0.0.1",
    author="Anastasia Aizman",
    author_email="anastasia.aizman@gmail.com",
    description="RNN — coloring words",
    keywords="namecolor",
    py_modules=["namecolor"],
    url="",
    long_description=read("README"),
    cmdclass={'install': Install}
)
