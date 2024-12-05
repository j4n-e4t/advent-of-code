rules = []
prints = []
valid_sequences = []
total = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if "|" in line:
            before, after = line.split("|")
            rules.append((int(before), int(after)))
        elif "," in line and line:
            prints.append([int(x) for x in line.split(",")])

    for sequence in prints:
        valid = True
        for before, after in rules:
            if before in sequence and after in sequence:
                if sequence.index(before) > sequence.index(after):
                    valid = False
                    break
        total += sequence[int(len(sequence)/2)] if valid else 0
print(total)
