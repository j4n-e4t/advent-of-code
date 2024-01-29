# Advent of Code 2015 - Day 1 - Part 1

FILE = "../input.txt"


def main():
    floor = 0
    with open(FILE, 'r') as f:
        data = f.read()
        for c in data:
            match c:
                case '(':
                    floor += 1
                case ')':
                    floor -= 1
                case _:
                    continue
    print("Destination floor: " + floor.__str__())


if __name__ == "__main__":
    main()
