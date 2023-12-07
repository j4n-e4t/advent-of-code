# Advent of Code 2023 - Day 4 - Part 1

FILE = "../input.txt"

def parse_line(line):
    line = line.split(":")[1].replace("\n", "")
    winning_numbers = [x for x in line.split("|")[0].split(" ") if x != "" and x != " "]
    all_numbers = [x for x in line.split("|")[1].split(" ") if x != "" and x != " "]
    return winning_numbers, all_numbers


def check_winning_numbers(winning_numbers, all_numbers):
    count = 0
    for number in all_numbers:
        if number in winning_numbers:
            count += 1
    return count


def calculate_points(points):
    if points == 0:
        return 0
    return pow(2, points - 1)

def main():
    with open(FILE, "r") as f:
        total_points = 0
        for line in f.readlines():
            winning_numbers, all_numbers = parse_line(line)
            total_points += calculate_points(check_winning_numbers(winning_numbers, all_numbers))
    print("TOTAL POINTS: " + total_points.__str__())

if __name__ == "__main__":
    main()
