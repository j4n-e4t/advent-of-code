floor = 0
with open("input_1.txt", "r") as f:
    data = f.read()
    for c in data:
        match c:
            case "(":
                floor += 1
            case ")":
                floor -= 1
            case _:
                continue
print(floor.__str__())
