# Advent of Code 2023 - Day 8 - Part 1

FILE = "../input.txt"


def parse_file():
    directions = ""
    nodes = {}
    with open(FILE, "r") as f:
        lines = f.readlines()
        directions = lines[0]
        for line in lines[2:]:
            nodes[line.strip().split(" = ")[0]] = (
                line.strip().split(" = ")[1].replace("(", "").replace(")", "")
            )
    return directions, nodes


def go(current_pos):
    if current_pos != "ZZZ":
        direction = "L"
        next_pos = get_next_node(direction, current_opts)
        go(next_pos)

    print(next_pos)


def get_next_node(direction, opts):
    if direction == "L":
        return opts.split(", ")[0]
    else:
        return opts.split(", ")[1]


def main():
    #directions, nodes = parse_file()
    #print(directions)
    #print(nodes)
    go("AAA")


if __name__ == "__main__":
    main()
