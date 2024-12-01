left_list = []
right_list = []
similarities = []

with open("input.txt") as f:
    for line in f:
        left, right = line.strip().split("   ")
        left_list.append(left)
        right_list.append(right)

for i in range(len(left_list)):
    similarities.append(int(left_list[i]) * right_list.count(left_list[i]))

print(sum(similarities))
