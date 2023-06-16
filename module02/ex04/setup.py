import setuptools

setuptools.setup(
    name = 'my_minipack',
    version = '1.0.0',
    description = 'How to create a package in python.',
    author = 'sojung',
    author_email = 'sojung@student.42.fr',
    license = 'MIT',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Students',
        'Topic :: Education',
        'Topic :: HowTo',
        'Topic :: Package',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    url = 'None',
    package_dir={'': 'src'},
    packages = setuptools.find_packages(where='src'),
    python_requires = '>=3.7',
)