rules = []
prints = []
valid_sequences = []
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
        valid_sequences.append(sequence) if check_sequence(sequence, rules) else None

    for seq in valid_sequences:
        total += seq[len(seq) // 2]

print(total)
