from World import World
from State import State
import collections

def load(file):
    file_object = open(file, 'r')
    stage = 0
    list_states = collections.OrderedDict()
    counter = 0
    actions = 0
    probabilities = []
    movements = collections.OrderedDict()
    terminal = []
    gamma = 0
    start = ""
    for lines in file_object:
        lines = lines.replace('\n', '')
        aux_identify = lines.split()
        if stage != 2:
            for x in aux_identify:
                if list_states:
                    if x in list_states:
                        stage = 1
        if stage == 0:
            if len(lines) > 2:
                candidate = lines.split()
                name = candidate[0]
                reward = int(candidate[1])
                utility = 0
                state = State(utility, reward)
                list_states[name] = state
        elif stage == 2:
            candidate = lines.split()
            if len(candidate) > 2:
                movements[candidate[0] + candidate[1]] = candidate[2]
            else:
                if counter == 0:
                    gamma = float(lines)
                    counter += 1
                elif counter == 1:
                    start = lines
                    counter += 1

        elif stage == 1:
            if counter == 0:
                terminal = lines.split()
                counter += 1
            elif counter == 1:
                counter += 1
                actions = int(lines) + counter
            elif counter < actions:
                probabilities.append(lines)
                counter += 1
            else:
                stage = 2
                counter = 0
    world = World(list_states, terminal, movements, probabilities, gamma, start)
    return world












