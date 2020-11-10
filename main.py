import json

import flask
from flask import request

from fsm import FiniteStateMachine
from fsm import State

app = flask.Flask(__name__)
app.config["DEBUG"] = True

fsm = FiniteStateMachine(State('uninitialized'))


@app.route('/fsm', methods=['GET'])
@app.route('/fsm/current-state', methods=['GET'])
def get_current_state():
    return json.dumps({"currentState": fsm.get_current_state().current_state_name})


@app.route('/fsm/valid-actions', methods=['GET'])
def get_valid_actions():
    return json.dumps({"validActions": fsm.list_valid_actions()})


@app.route('/fsm', methods=['POST'])
def post_fsm():
    args = request.args

    if "action_name" in args:
        action_name = args["action_name"]
        result_msg = fsm.perform_action(action_name)
        if result_msg is None:
            return json.dumps({" new currentState": fsm.get_current_state().current_state_name})
        else:
            return json.dumps({"error_message": result_msg}), 405

    return initialize_fsm()


def initialize_fsm():
    req_data = request.get_json()

    global fsm
    fsm = FiniteStateMachine(State(req_data['start']))

    for transition in req_data['transitions']:
        print_transition_data(transition)
        fsm.add_transition(transition['currentState'],
                           transition['nextState'],
                           transition['actionName'])

    return json.dumps(req_data), 201


def print_transition_data(transition):
    print("\n")
    print("One transition's currentState:" + transition['currentState'])
    print("One transition's currentState:" + transition['nextState'])
    print("One transition's currentState:" + transition['actionName'])


if __name__ == '__main__':
    app.run()  # run our Flask app
