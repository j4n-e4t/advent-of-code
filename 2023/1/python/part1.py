# Advent of Code - 2023 - Day 1 - Part 1

FILE = "../input.txt"


def get_numbers(line):
    numbers_in_line = []
    for char in line:
        if char.isdigit():
            numbers_in_line.append(char)
    return numbers_in_line


def main():
    sum_numbers = 0
    with open(FILE, "r") as f:
        for line in f.readlines():
            print(line.__str__().strip())
            numbers = get_numbers(line)
            if len(numbers) < 1:
                continue
            else:
                sum_numbers += int("{}{}".format(numbers[0], numbers[-1]))
    print("SUM: " + sum_numbers.__str__())


if __name__ == "__main__":
    main()
