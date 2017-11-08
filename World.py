
class World:

    def __init__(self, states, terminal_states, movement, probabilities, gamma, start):
        self.states = states
        self.terminal_states = terminal_states
        self.movement = movement
        self.probabilities = probabilities
        self.gamma = gamma
        self.start = start
        self.probs_dict = {}
        self.define_probabilities()
        self.terminal_utilities()

    def move(self, state, action):
        return self.movement[state + action]

    def define_probabilities(self):
        for probs in self.probabilities:
            aux = probs.split(" ")
            action = aux[0]
            self.probs_dict['N' + '|' + action] = aux[1]
            self.probs_dict['E' + '|' + action] = aux[2]
            self.probs_dict['S' + '|' + action] = aux[3]
            self.probs_dict['W' + '|' + action] = aux[4]

    def terminal_utilities(self):
        for terminals in self.terminal_states:
            self.states[terminals].utility = self.states[terminals].reward




