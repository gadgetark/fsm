class Transition:

    def __init__(self, current_state_name, next_state_name, action_name):
        self.current_state_name = current_state_name
        self.next_state_name = next_state_name
        """ Transition keyed by action_name """
        self.action_name = action_name


class State:

    def __init__(self, current_state_name):
        self.current_state_name = current_state_name
        self.transitions = {}

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

    def __init__(self, start_state):
        # when initializing it is safe to assume the current_state is the start_state
        self.current_state = start_state
        self.state_objects = {start_state.current_state_name: start_state}

    def add_transition(self, current_state_name, next_state_name, action_name):
        # self.current_state_name = current_state_name
        new_transition = Transition(current_state_name, next_state_name, action_name)
        new_state = self.create_new_state_if_none(current_state_name)
        new_state.add_transition(new_transition)
        self.state_objects[current_state_name] = new_state

    def create_new_state_if_none(self, current_state_name):
        if current_state_name in self.state_objects.keys():
            return self.state_objects[current_state_name]
        else:
            return State(current_state_name)

    def perform_action(self, action_name):
        if self.current_state.is_action_name_valid(action_name):
            # if the action_name is valid then transition the current_state to new state
            next_state_name = self.current_state.get_transition(action_name).next_state_name
            self.current_state = self.state_objects[next_state_name]
        else:
            print("The provided action_name is invalid")
            print("The valid actions are:",  self.list_valid_actions())

    def get_current_state(self):
        return self.current_state

    def list_valid_actions(self):
        # get current_state's transitions. The transitions are keyed by action_names
        return list(self.current_state.get_all_transitions().keys())


class FiniteStateMachine(IFiniteStateMachine):
    pass
