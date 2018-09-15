from setuptools import setup, find_packages

setup(
    name='Py-Paint',
    version='1.0.0',
    author='Luigi D. C. Soares',
    packages=find_packages(),
    install_requires=[
        'pyqt5==5.9',
        'numpy',
    ],
)
