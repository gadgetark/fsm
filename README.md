# fsm

# Software requirements to develop and execute the project
* python3
* virtualenv
* venv

# To setup the project for development
1. git clone the this fsm repo.
2. cd into fsm project repo root directory.
    * cd fsm
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
1. cd into fsm project repo root directory.
    * cd fsm
2. start the venv of this project
    * source venv/bin/activate 
3. Run the main.py
    * python main.py

# Send HTTP Request to the fsm Web API with curl
1. GET fsm:
    * curl --request GET 'http://127.0.0.1:5000/fsm'
2. GET valid-actions:
    * curl --request GET 'http://127.0.0.1:5000/fsm/valid-actions'
3. GET current-state:
    * curl --request GET 'http://127.0.0.1:5000/fsm/current-state'
4. POST the default fsm to initialize. The default json is provided by the documentation "Kinsa Backend Engineer Coding Exercise":
    * `curl --request POST 'http://127.0.0.1:5000/fsm' \
--header 'Content-Type: application/json' \
--data-raw '{
  "start": "state_a",
  "transitions": [
    {
      "currentState": "state_a",
      "nextState": "state_b",
      "actionName": "action_1"
    },
    {
      "currentState": "state_a",
      "nextState": "state_c",
      "actionName": "action_2"
    },
    {
      "currentState": "state_b",
      "nextState": "state_c",
      "actionName": "action_3"
    }
  ]
}
'`
5. POST action_name with query param value of "action_1" to the fsm:
    * `curl --request POST 'http://127.0.0.1:5000/fsm?action_name=action_1'` 
6. POST action_name with query param value of "action_2" to the fsm:
    * `curl  --request POST 'http://127.0.0.1:5000/fsm?action_name=action_2'` 
7. POST action_name with query param value of "action_3" to the fsm:
    * `curl  --request POST 'http://127.0.0.1:5000/fsm?action_name=action_3'` 
8. New POST json with only one state_c transition added to the default fsm, where action_3 would be valid when current_state is state_b
    * `curl --request POST 'http://127.0.0.1:5000/fsm' \
--header 'Content-Type: application/json' \
--data-raw '{
  "start": "state_a",
  "transitions": [
    {
      "currentState": "state_a",
      "nextState": "state_b",
      "actionName": "action_1"
    },
    {
      "currentState": "state_a",
      "nextState": "state_c",
      "actionName": "action_2"
    },
    {
      "currentState": "state_b",
      "nextState": "state_c",
      "actionName": "action_3"
    },
    {
      "currentState": "state_c",
      "nextState": "state_a",
      "actionName": "action_4"
    }
  ]
}'`
9. New POST json with all the needed state transitions added to the default fsm to complete bi-directional state transition. state_a => state_b, state_a => state_c,state_b => state_c, state_b => state_a, state_c => state_a, state_c => state_b
    * `curl --request POST 'http://127.0.0.1:5000/fsm' \
--header 'Content-Type: application/json' \
--data-raw '{
  "start": "state_a",
  "transitions": [
    {
      "currentState": "state_a",
      "nextState": "state_b",
      "actionName": "action_1"
    },
    {
      "currentState": "state_a",
      "nextState": "state_c",
      "actionName": "action_2"
    },
    {
      "currentState": "state_b",
      "nextState": "state_c",
      "actionName": "action_3"
    },
    {
      "currentState": "state_b",
      "nextState": "state_a",
      "actionName": "action_5"
    },
    {
      "currentState": "state_c",
      "nextState": "state_a",
      "actionName": "action_4"
    },
    {
      "currentState": "state_c",
      "nextState": "state_b",
      "actionName": "action_6"
    }
  ]
}
'`


    
    

    