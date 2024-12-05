rules = []
prints = []
valid_sequences = []
invalid_sequences = []
total = 0

def check_sequence(sequence, rules):
    for before, after in rules:
        if before in sequence and after in sequence:
            if sequence.index(before) > sequence.index(after):
                return False
    return True

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if "|" in line:
            before, after = line.split("|")
            rules.append((int(before), int(after)))
        elif "," in line and line:
            prints.append([int(x) for x in line.split(",")])

for sequence in prints:
    if not check_sequence(sequence, rules):
        invalid_sequences.append(sequence)

for seq in invalid_sequences:
    while True:
        swapped = False
        for before, after in rules:
            if before in seq and after in seq:
                before_i = seq.index(before)
                after_i = seq.index(after)
                if before_i > after_i:
                    seq[before_i], seq[after_i] = seq[after_i], seq[before_i]
                    swapped = True
        if not swapped:
            break

    total += seq[len(seq) // 2]

print(total)
