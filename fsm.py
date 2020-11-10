class Transition:

    def __init__(self, current_state_name, next_state_name, action_name):
        self.current_state_name = current_state_name
        self.next_state_name = next_state_name
        """ Transition keyed by action_name """
        self.action_name = action_name


class State:
    transitions = {}

    def __init__(self, current_state_name):
        self.current_state_name = current_state_name

    def add_transition(self, transition):
        self.transitions[transition.action_name] = transition

    def is_action_name_valid(self, action_name):
        if action_name in self.transitions.keys():
            return True
        else:
            return False

    def get_transition(self, action_name):
        return self.transitions[action_name]

    def get_all_transitions(self):
        return self.transitions


class IFiniteStateMachine:
    state_objects = {}

    def __init__(self, current_state):
        self.current_state = current_state

    def add_transition(self, current_state_name, next_state_name, action_name):
        # self.current_state_name = current_state_name
        new_transition = Transition(current_state_name, next_state_name, action_name)
        new_state = State(current_state_name)
        new_state.add_transition(new_transition)
        self.state_objects[current_state_name] = new_state

    def perform_action(self, action_name):
        if self.current_state.is_action_name_valid(action_name):
            # if the action_name is valid then transition the current_state to new state
            next_state_name = self.current_state.get_transition(action_name).next_state_name
            self.current_state = self.state_objects[next_state_name]
        else:
            print("The provided action_name is invalid")
            print("The valid actions are:" + self.list_valid_actions())

    def get_current_state(self):
        return self.current_state

    def list_valid_actions(self):
        return list(self.current_state.get_all_transitions())


class FiniteStateMachine(IFiniteStateMachine):
    pass
