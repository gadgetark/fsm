# fsm

# requirements to develop and execute the project
* python3
* virtualenv
* venv

# To setup the project for development
1. git clone the this fsm repo.
2. cd into fsm. 
3. Make sure the python3 is installed
4. Install virtualenv:
    * pip install virtualenv
5. Add the virtualenv to PATH.
6. Create the venv under the fsm project directory. Note: Make sure you use a valid path to your python3 installation.
    * virtualenv -p /usr/bin/python3 venv
7. Start working with this fsm project under venv
    * source venv/bin/activate 
8. Install the project python requirements:
    * pip install -r requirements.txt
9. Update new requirements added to the project if any.
    * pip freeze > requirements.txt


# To run the project
1. cd into the fsm project directory
2. python main.py