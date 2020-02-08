import math

totalfuel = 0
with open("input.txt") as fp:
    cnt = 0
    for line in fp:
        inp = int(line)
        while inp > 0:
            inp = math.floor(inp / 3) - 2
            if inp > 0:
                totalfuel = totalfuel + inp

print(totalfuel)