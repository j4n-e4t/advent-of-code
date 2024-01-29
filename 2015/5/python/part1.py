# Advent of Code 2015 - Day 5 - Part 1

FILE = "../input.txt"


def main():
    nice_strings = 0
    with open(FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if check_line(line):
                nice_strings += 1
    print("Nice strings: " + nice_strings.__str__())


def check_line(line):
    vowels = ["a", "e", "i", "o", "u"]
    bad_patterns = ["ab", "cd", "pq", "xy"]
    vowel_count = 0
    is_nice = False

    for c in line:
        vowel_count += 1 if c in vowels else 0

    if vowel_count < 3:
        return is_nice

    for pattern in bad_patterns:
        if pattern in line:
            return is_nice

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            is_nice = True
            break

    return is_nice


if __name__ == "__main__":
    main()
