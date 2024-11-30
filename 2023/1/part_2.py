# !!! Does not work !!!

NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_numbers(line: str) -> list:
    numbers_in_line = []
    for char in line:
        if char.isdigit():
            numbers_in_line.append(int(char))
    return numbers_in_line


def convert_number_word(line: str) -> str:
    for key, value in NUMBERS.items():
        line = line.replace(key, str(value))
    return line


def main() -> None:
    sum_numbers = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
            line = convert_number_word(line)
            print(line)
            numbers = get_numbers(line)
            print(numbers)
            if len(numbers) <= 1:
                continue
            else:
                first_number = numbers[0]
                last_number = numbers[-1]
                two_diget_number = "{}{}".format(first_number, last_number)
                print(two_diget_number)
                sum_numbers += int(two_diget_number)
            print("---")
        print("SUM: " + sum_numbers.__str__())


if __name__ == "__main__":
    main()
