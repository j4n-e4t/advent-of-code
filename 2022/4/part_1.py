count = 0
with open("input.txt", "r") as file:
    for line in file:
        start1, end1 = line.split(",")[0].split("-")
        start2, end2 = line.split(",")[1].split("-")

        start1, end1, start2, end2 = int(start1), int(end1), int(start2), int(end2)

        if start1<=start2 and end2<=end1 or start2<=start1 and end1<=end2:
            count += 1

print(count)
