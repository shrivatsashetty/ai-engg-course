
# Python Virtual Envs

## Create a Virtual Environment
```sh
# In Linux or MacOS
python3 -m venv .venv

# In Windows
python -m venv .venv
```

## Activate the Virtual Environment
```sh
# on mac os or linux
source .venv/bin/activate

# On Windows CMD
.\.venv\Scripts\activate.bat

# on Windows Powershell
.\.venv\Scripts\Activate.ps1 
```

## Deactivate Virtual Environment

Use the below command in your terminal to deactivate the selected Python Virtual Environment.

```sh
deactivate
```

## Install Packages
```sh
# install an individual package
pip install requests

# running pip as a python module.
# Sometimes required to install the package in the current Python environment.
python -m pip install openai

# Call the venv's pip explicitly
.venv/bin/python -m pip install openai

# install from a requirements file
pip install -r requirements.txt
```

## Using a requirements file
Create a file with name `requirements.txt`
```sh
touch requirements.txt
```
Put the names of all the packages required for your project along with their version within the file. The content should look something like this
```txt
requests==2.34.2
Flask==3.1.3
numpy>=1.24.0
```

Install packages from the `requirements.txt` file
```sh
pip install -r requirements.txt
```
The option `-r` stands for `read`

To dump every package currently installed in your active Python environment into the requirements file:
```sh
# overrwrites the existing file or creates if not exists.
pip freeze > requirements.txt
```
You can also run the above command after installing a new package inside your python environment so that it's updated.

## List Installed Packages
Use the below command to list all the packages installed in the current Python Environment.

```sh
pip list
```

## Check Python Interpreter

Use any of the below commands to check which Python interpreter is being used:

```sh
which python

which pip

python -c "import sys; print(sys.prefix)"

ls -l .venv/bin/python
```

