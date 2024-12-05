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
    swapped = False
    while not swapped:
        for before, after in rules:
            if before in seq and after in seq:
                if seq.index(before) > seq.index(after):
                    seq[seq.index(before)], seq[seq.index(after)] = seq[seq.index(after)], seq[seq.index(before)]
                    swapped = True
        swapped = not swapped

    total += seq[len(seq) // 2]

print(total)
