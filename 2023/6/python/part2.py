# Advent of Code 2023 - Day 6 - Part 2

FILE = "../input.txt"


def main():
    time, distances = parse_input_file()
    print(
        "Possible holding durations: "
        + calculate_possible_options(
            int(f"{time[0]}{time[1]}{time[2]}{time[3]}"),
            int(f"{distances[0]}{distances[1]}{distances[2]}{distances[3]}"),
        ).__str__()
    )


def parse_input_file():
    with open(FILE, "r") as f:
        first_line = f.readline().split()
        second_line = f.readline().split()
        first_line.pop(0)
        second_line.pop(0)
        first_line = list(map(int, first_line))
        second_line = list(map(int, second_line))

    return first_line, second_line


def calculate_possible_options(time, distance):
    options = []
    for i in range(1, time):
        if ((time - i) * i) > distance:
            options.append(i)
    return options.__len__()


if __name__ == "__main__":
    main()
