from setuptools import setup
import re
VERSIONFILE="propti/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
    
setup(
    name='propti',
    version=verstr,    
    description="PROPTI is a Python module, written in Python 3.x. It provides a frame work for inverse modelling (or optimisation) of parameters in computer simulation. It's focused on handling the communication between simulation software and optimisation algorithms. Up to now, "+'"'+'a Statistical Parameter Optimization Framework for Python"' + "SPOTPY is used to provide a library of algorithm implementations. The Fire Dynamics Simulator FDS is used for the simulation side of things.",
    url='https://github.com/FireDynamics/propti',
    author='Tristan Hehnen',
    author_email='tristan.hehnen@gmail.com',
    license='MIT',
    packages=['propti'],
    
    include_package_data=True,
    install_requires=[ 'mpi4py',
                       'spotpy',    
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
