winners = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

my_score = 0

with open("input_1.txt", "r") as input:
    for line in input:
        my_score += scores[line[2]] + winners[line.strip()]

print(my_score)
