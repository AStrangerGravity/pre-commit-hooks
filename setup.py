from setuptools import find_packages
from setuptools import setup

setup(
    name='pre-commit-hooks',
    description='Some out-of-the-box hooks for pre-commit',
    url='https://github.com/AStrangerGravity/pre-commit-hooks',
    version='0.0.1',

    author='John Austin',
    author_email='john@astrangergravity.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'forbid_crlf = pre_commit_hooks.forbid_crlf:main',
            'remove_crlf = pre_commit_hooks.remove_crlf:main',
            'forbid_tabs = pre_commit_hooks.forbid_tabs:main',
            'remove_tabs = pre_commit_hooks.remove_tabs:main',
            'end_of_file_fixer = pre_commit_hooks.end_of_file_fixer:main',
            'trailing_whitespace_fixer = pre_commit_hooks.trailing_whitespace_fixer:main',
        ],
    },
)
