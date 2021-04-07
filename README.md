# Whack-A-Mole Polymorphic  Attack!

This repository was created for the Spring2021 CSE 4471 9:35am Dr. Jones class at the Ohio State University. This repository belongs to team **Foxbat**. It is not for reference outside team members, professors, and graders.

This project was divided into specialization(s). Rocky, Benjamin, and Jonathan worked primarily together on the pygame aspect of this project while Parker tackled the C virus. For further info, check the source files. Note: Pushes to git repo are not indications of authorship of code.

## Installation

Below are important steps to installing this program. Read them carefully.

### Virtual env

We have created a virtual environment for convenience in running this application. A virtual environment mimics a python environment but abstract packages to a directory instead of in a package manager. This allows uniform installations of packages and ensures the same environment is used even over git.

### Running a virtual environment

A virtual environment should be run each time a project is worked on. To activate the virtual environment follow the steps [here](https://docs.python.org/3/library/venv.html). In general it is as follows

| **Platform**    | **Shell**       | **Command**  |
| -------------   |:---------------:|        -----:|
| POSIX           | bash/zsh        | $ source <venv>/bin/activate |
|                 | fish            | $ source <venv>/bin/activate.fish |
|                 | csh/tcsh        | $ source <venv>/bin/activate.csh|
|                 | PowerShell Core | $ <venv>/bin/Activate.ps1|
| WINDOWS         | cmd.exe         |   C:\> <venv>\Scripts\activate.bat |
|                 | PowerShell      |   PS C:\> <venv>\Scripts\Activate.ps1|

### Pip requirements

In order to run the python program, dependencies must be installed. These can be installed with a simple command:

`pip install -r requirements.txt`

## Execution

These steps are for executing the program.

### Main

To run the PyGame program run `python3 main.py` from the command line.
