# Advent of Code 2015 - Day 1 - Part 1

import hashlib

INPUT = "yzbqklnj"


def main():
    i = 0
    while True:
        if (hashlib.md5((INPUT + i.__str__()).encode('utf-8')).hexdigest().startswith("00000")):
            print(i)
            break
        i += 1


if __name__ == "__main__":
    main()
