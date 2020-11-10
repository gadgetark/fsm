# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm again')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import json

import flask
from flask import request

from fsm import FiniteStateMachine
from fsm import State

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/fsm', methods=['POST'])
def initialize_fsm():
    req_data = request.get_json()
    print("start:" + req_data['start'])
    print("transitions:" + json.dumps(req_data['transitions']))

    # return json.dumps({"success": True}), 201

    print("PRINTING:")
    # print(req_data['transitions'][0]['currentState'])
    fsm = FiniteStateMachine(State(req_data['start']))

    for transition in req_data['transitions']:
        print("One transition's currentState:" + transition['currentState'])
        fsm.add_transition(transition['currentState'],
                           transition['nextState'],
                           transition['actionName'])
    return json.dumps(req_data), 201


if __name__ == '__main__':
    app.run()  # run our Flask app
