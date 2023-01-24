from setuptools import setup, find_packages

setup(
    name='my_minipack',
    version='1.0',
    description='My first python package',
    author='lsuardi',
    author_email='lsuardi@student.42.fr',
    packages=find_packages(),
    install_requires=[],
    license='MIT',
    url=None,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Students',
        'Topic :: Education',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
