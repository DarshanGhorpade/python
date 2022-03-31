# Author: Darshan Ghorpade
# Location: Earth
# Date: 31/03/2022

# Virtual Environment in Python
# An environment that is same as the system interpreter but is isolated from the other python environments on the system.

'''
Installation

To use virtual environments, we write
pip install virtualenv          #Installs the package
We create a new environment using:
virtualenv myprojectenv             #Creates a new venv
The next step after creating the virtual environment is to activate it.
We can now use this virtual environment as a separate python installation.
'''

# For MacOS/linux users: source myprojectenv/bin/activate
# For windows powershell users: .\myprojectenv\Scripts\activate.ps1
# https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows

import flask
import pandas as pd




# pip freeze command
'''
pip freeze returns all the packages installed in a given python environment along with the versions.
“pip freeze > requirements.txt”
The above command creates a file named requirements.txt in the same directory containing the output of pip freeze.
We can distribute this file to other users and they can recreate the same environment using:
pip install –r requirements.txt
'''