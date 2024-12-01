left_list = []
right_list = []
distances = []

with open("input.txt") as f:
    for line in f:
        left, right = line.strip().split("   ")
        left_list.append(left)
        right_list.append(right)
    left_list.sort()
    right_list.sort()


for i in range(len(left_list)):
    distances.append(abs(int(left_list[i]) - int(right_list[i])))

print(sum(distances))
