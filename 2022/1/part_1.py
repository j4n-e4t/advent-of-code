with open("input.txt") as f:
    lines = f.readlines()
    blocks = "".join(lines).split("\n\n")
    blocks = [block.replace("\n", " ") for block in blocks]
    total_sums = []
    biggest = 0

    for block in blocks:
        sum = 0
        if block == "":
            continue
        block = block.split(" ")
        for i in range(block.__len__()):
            sum += int(block[i])
        total_sums.append(sum)

    for i in range(total_sums.__len__()):
        if total_sums[i] > biggest:
            biggest = total_sums[i]

    print(biggest.__str__())
