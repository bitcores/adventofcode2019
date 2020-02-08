import re
import copy

star = []
starvel = []
# starting positions gathered
#with open("input12test.txt") as fp:
with open("input12.txt") as fp:
    cnt = 0
    for line in fp:
        tmp = re.findall(r'-?\d+', line)
        star.append(list(map(int, tmp)))

pos = copy.deepcopy(star)
vel = []
velc = []
for y in range(len(pos[0])):
    velc.append(0)
for x in range(len(pos)):
    vel.append(copy.deepcopy(velc))
starvel = copy.deepcopy(vel)

for q in range(10):
    # do gravity calc
    inst = copy.deepcopy(pos)
    newinst = copy.deepcopy(pos)
    newvel = copy.deepcopy(vel)

    for w in range(len(pos[0])):
        for e in range(len(pos)):
            for r in range(len(pos)):
                if e < r:
                    if inst[e][w] > inst[r][w]:
                        newinst[e][w] = newinst[e][w] - 1
                        newinst[r][w] = newinst[r][w] + 1
                    elif inst[e][w] < inst[r][w]:
                        newinst[e][w] = newinst[e][w] + 1
                        newinst[r][w] = newinst[r][w] - 1
    
    for e in range(len(pos)):
        for w in range(len(pos[0])):
            pos[e][w] = newinst[e][w] + vel[e][w]
    
    # do velocity calc
    for e in range(len(pos)):
        for w in range(len(pos[0])):
            newvel[e][w] = pos[e][w] - inst[e][w]

    vel = copy.deepcopy(newvel)

#calculate energy
tenergy = 0
for e in range(len(pos)):
    pot = 0
    kin = 0
    for w in range(len(pos[0])):
        pot = pot + abs(pos[e][w])
        kin = kin + abs(vel[e][w])
    tenergy = tenergy + (pot * kin)

print(pos)
print(vel)
print(tenergy)

# fuck this part and fuck calculating the LCM myself
pos = copy.deepcopy(star)
vel = copy.deepcopy(starvel)
print(pos)
print(vel)
xyzsteps = []
steps = 0
c = 0
while c < 3:
    # do gravity calc
    inst = copy.deepcopy(pos)
    newinst = copy.deepcopy(pos)
    newvel = copy.deepcopy(vel)

    for e in range(len(pos)):
        for r in range(len(pos)):
            if e < r:
                if inst[e][c] > inst[r][c]:
                    newinst[e][c] = newinst[e][c] - 1
                    newinst[r][c] = newinst[r][c] + 1
                elif inst[e][c] < inst[r][c]:
                    newinst[e][c] = newinst[e][c] + 1
                    newinst[r][c] = newinst[r][c] - 1
    
    for e in range(len(pos)):
            pos[e][c] = newinst[e][c] + vel[e][c]
    
    # do velocity calc
    for e in range(len(pos)):
            newvel[e][c] = pos[e][c] - inst[e][c]

    vel = copy.deepcopy(newvel)
    if pos == star and vel == starvel:
        xyzsteps.append(steps+1)
        c = c + 1
        steps = 0
    else:
        steps = steps + 1

print(xyzsteps)
