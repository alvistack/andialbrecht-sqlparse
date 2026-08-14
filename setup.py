from setuptools import setup

setup(
    name='sqlparse',
    version='0.6.0',
    description='A non-validating SQL parser.',
    author_email='Andi Albrecht <albrecht.andi@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Database',
        'Topic :: Software Development',
    ],
    extras_require={
        'dev': [
            'build',
        ],
        'doc': [
            'furo',
            'sphinx',
        ],
    },
    entry_points={
        'console_scripts': [
            'sqlformat = sqlparse.__main__:main',
        ],
    },
    packages=[
        'sqlparse',
        'sqlparse.engine',
        'sqlparse.filters',
    ],
)
