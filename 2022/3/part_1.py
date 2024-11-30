def get_two_compartments(rucksack: str):
    return (
        rucksack[: len(rucksack) // 2],
        rucksack[len(rucksack) // 2 :],
    )


def get_similar_items(compartment_1, compartment_2):
    duplicates = []
    for char in compartment_1:
        if char in compartment_2 and char not in duplicates:
            duplicates.append(char)
    return duplicates


weights = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

sum = 0

with open("input_1.txt", "r") as input:
    for line in input:
        first, second = get_two_compartments(line)
        for item in get_similar_items(first, second):
            sum += weights[item]

print(sum)
