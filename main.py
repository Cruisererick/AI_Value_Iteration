import Load_Map


def main():
    file = "Maps//fig_17_3.txt"
    world = Load_Map.load(file)
    print(world.probs_dict["N|N"])


if __name__ == '__main__':
    main()
