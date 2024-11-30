with open("input.txt") as f:
    lines = f.readlines()
    blocks = "".join(lines).split("\n\n")
    blocks = [block.replace("\n", " ") for block in blocks]
    total_sums = []
    top_3 = []
    top_3_sums = 0

    for block in blocks:
        sum = 0
        if block == "":
            continue
        block = block.split(" ")
        for i in range(block.__len__()):
            sum += int(block[i])
        total_sums.append(sum)

    for i in range(total_sums.__len__()):
        if top_3.__len__() < 3:
            top_3.append(total_sums[i])
        else:
            if total_sums[i] > min(top_3):
                top_3[top_3.index(min(top_3))] = total_sums[i]

    for i in range(top_3.__len__()):
        top_3_sums += top_3[i]

    print(top_3_sums.__str__())
