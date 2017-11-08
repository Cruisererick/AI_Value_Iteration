import Load_Map
from State import State


def main():
    file = "Maps//tunnel_a2_g10_r1.txt"
    world = Load_Map.load(file)
    print(world.states['b4'])
    e = 10**(-5)
    utilities, directions = value_iteration(world, e)
    print(utilities, directions)


def create_csv(file, utilities, directions):
    filename = file[:len(file)-4]
    filename += "_result.txt"



def value_iteration(world, e):
    U = {}
    U_prime = {}
    maximum_change = 0
    policy_dict = {}

    for state in world.states:
        U_prime[state] = world.states[state].utility

    while True:
        U = U_prime.copy()
        maximum_change = 0

        for state in world.states:
            max_number, direction = get_max(world, state, U)
            U_prime[state] = world.states[state].reward + (world.gamma * max_number)
            policy_dict[state] = direction
            number = abs(U_prime[state] - U[state])
            if number > maximum_change:
                maximum_change = abs(U_prime[state] - U[state])

        compare = (e * (1 - world.gamma)/world.gamma)
        if maximum_change <= compare:
            break
    return U, policy_dict


def get_max(world, state, U):
    numbers = []
    for actions in world.probabilities:
        try:
            target_state_N = world.movement[state + 'N']
            target_state_E = world.movement[state + 'E']
            target_state_S = world.movement[state + 'S']
            target_state_W = world.movement[state + 'W']
        except KeyError:
            return 0, None
        prob_n = world.probs_dict['N|' + actions[0]]
        prob_e = world.probs_dict['E|' + actions[0]]
        prob_s = world.probs_dict['S|' + actions[0]]
        prob_w = world.probs_dict['W|' + actions[0]]
        north = (U[target_state_N] * float(prob_n))
        east = (U[target_state_E] * float(prob_e))
        south = (U[target_state_S] * float(prob_s))
        west = (U[target_state_W] * float(prob_w))
        numbers.append(north + east + south + west)

    maxi = max(numbers)
    direction = numbers.index(maxi)

    if direction == 0:
        direction = "N"
    elif direction == 1:
        direction = "E"
    elif direction == 2:
        direction = "S"
    elif direction == 3:
        direction = "W"

    return maxi, direction



if __name__ == '__main__':
    main()
