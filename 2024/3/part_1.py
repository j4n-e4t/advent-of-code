import re

sum = 0

with open("input.txt") as file:
    for i in re.findall(r'mul\(\d{1,3},\d{1,3}\)', file.read()):
      a, b = i.replace("mul", "").replace("(", "").replace(")", "").split(",")
      sum += int(a) * int(b)

print(sum)
