found = False
with open("input.txt") as file:
    line = file.readline().strip()
    for i in range(len(line)):
        if (not found) and i-3>=0 and len(set([line[i-j] for j in range(4)]))==4:
            print(i+1)
            found = True
