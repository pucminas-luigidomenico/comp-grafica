from setuptools import setup, find_packages

setup(
    name='Py-Paint',
    version='1.0.0',
    author='Luigi D. C. Soares',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
        'numpy',
    ],
    hiddenimports=[
        'PyQt5.sip',
    ]
)
