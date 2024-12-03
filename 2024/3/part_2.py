import re

count = 0

with open("input.txt","r+t") as file:
    dosequenz = "do()"
    dontsequenz = "don't()"
    enabled = True
    for line in file:
        i = 0
        while i < len(line)-11:
            enabled = True if line[i:i+len(dosequenz)] == dosequenz else False if line[i:i+len(dontsequenz)] == dontsequenz else enabled


            z = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line[i:i+15])
            if z and enabled:
                z = z[0]
                a, b = z.replace("mul(", "").replace(")", "").split(",")
                i = ( line.find(z) + len(z))-1
                count += int(a) * int(b)
            i += 1
print(count)
