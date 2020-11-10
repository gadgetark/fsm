# test the fsm is initialized successfully
# Requirement: start this fsm main.py web api app before running this test
# To start this fsm app: 1) cd fsm 2) source venv/bin/activate 3) python main.py

import requests
import json


def test_default_fsm_initialized():
    url = 'http://127.0.0.1:5000/fsm'
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {
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

    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

    assert resp.status_code == 201

    print(resp.text)

    test_fsm_current_state("state_a")
    test_fsm_valid_actions(["action_1", "action_2"])

    test_post_action_name("action_1")
    test_fsm_current_state("state_b")
    test_fsm_valid_actions(["action_3"])


def test_full_fsm_initialized():
    url = 'http://127.0.0.1:5000/fsm'
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {
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

    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

    assert resp.status_code == 201

    print(resp.text)

    test_fsm_current_state("state_a")
    test_fsm_valid_actions(["action_1", "action_2"])

    test_fsm_current_state("state_a")
    test_post_action_name("action_1")
    test_fsm_current_state("state_b")
    test_fsm_valid_actions(["action_3", "action_5"])

    test_fsm_current_state("state_b")
    test_post_action_name("action_3")
    test_fsm_current_state("state_c")
    test_fsm_valid_actions(["action_4", "action_6"])


def test_fsm_current_state(expected_current_state):
    url = 'http://127.0.0.1:5000/fsm/current-state'
    resp = requests.get(url)

    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['currentState'] == expected_current_state

    print(resp.text)


def test_fsm_valid_actions(expected_valid_actions):
    url = 'http://127.0.0.1:5000/fsm/valid-actions'
    resp = requests.get(url)

    assert resp.status_code == 200
    resp_body = resp.json()
    print(resp_body['validActions'])
    assert (all(expected_valid_actions for x in resp_body['validActions']))


def test_post_action_name(action_name):
    url = 'http://127.0.0.1:5000/fsm'
    headers = {'Content-Type': 'application/json'}
    params = {'action_name': action_name}

    resp = requests.post(url, headers=headers, params=params)

    assert resp.status_code == 200
