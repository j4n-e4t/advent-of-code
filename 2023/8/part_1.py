instructions = []
locations = {}
steps = 0
current_location = "AAA"


with open("input.txt") as f:
    lines = f.readlines()

    for char in lines[0].strip():
        instructions.append(char)

    for line in lines[2:]:
        line = line.strip().split(" = ")
        locations[line[0]] = line[1].replace("(", "").replace(")", "").replace(",", "")

while current_location != "ZZZ":
    for instruction in instructions:
        options = locations[current_location].split(" ")
        match instruction:
            case "L":
                current_location = options[0]
            case "R":
                current_location = options[1]
        steps += 1

print(steps)
