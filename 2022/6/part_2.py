found = False
with open("input.txt") as file:
    line = file.readline().strip()
    for i in range(len(line)):
        if (not found) and i-13>=0 and len(set([line[i-j] for j in range(14)]))==14:
            print(i+1)
            found = True
