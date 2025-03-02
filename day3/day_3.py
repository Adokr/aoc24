import re

with open("day3/input.txt", "r") as file:
    content = file.read()

multiplications = re.findall("mul\([0-9]*,[0-9]*\)|do\(\)|don\'t\(\)", content)
enabled = True
score = 0
for el in multiplications:
    if el == 'do()':
        enabled = True
    elif el == "don't()":
        enabled = False
    else:
        if enabled:
            tmp = el.strip("mul(").strip(")").split(",")
            score += int(tmp[0])*int(tmp[1])
    
print(score)