from setuptools import find_packages, setup

setup(
    name='euclid',
    version='1.0.dev0',

    py_modules=['euclid'],

    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'numpy',
        'pytest',
    ],

    author='Thomas Waters',
    author_email='twaters117@gmail.com',
    description='2D and 3D vector, matrix, quaternion and geometry and graphics module',
    license='LGPLv2+',
    keywords=['geometry'],
    url='https://github.com/evelios/pyeuclid',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        ('License :: OSI Approved :: '
         'GNU Lesser General Public License v2 or later (LGPLv2+)'),
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
