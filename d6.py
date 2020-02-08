orbc = 0
orbits = {}
psan = []
pyou = []

def countorbits(key, depth, psantmp, pyoutmp):
    global orbits
    global orbc
    global psan
    global pyou
    
    if 'SAN' in orbits[key]:
        psan = psantmp[:]
    elif 'YOU' in orbits[key]:
        pyou = pyoutmp[:]

    for o in orbits[key]:
        orbc = orbc + depth
        
        if o in orbits:
            psantmp.append(o)
            pyoutmp.append(o)
            countorbits(o, depth+1, psantmp[:], pyoutmp[:])
            psantmp.pop(-1)
            pyoutmp.pop(-1)

def counttransfer():
    global psan
    global pyou

    tsan = []
    tyou = []

    r = len(psan)
    if len(pyou) < r:
        r = len(pyou)
    for n in range(r-1):
        if (psan[n] == pyou[n] and psan[n+1] != pyou[n+1]) or n == r-2:
            tsan = psan[n+1:]
            tyou = pyou[n+1:]
            break
    
    return len(tyou) + len(tsan)


with open("input6.txt") as fp:
    for line in fp:
        orb = line.split(")")
        if not orb[0] in orbits:
            orbits[orb[0]] = []
        orbits[orb[0]].append(orb[1].strip())

countorbits('COM', 1, [], [])


trans = counttransfer()

#print(orbits)
print(orbc)
print(trans)
#print('Path to Santa: ',psan)
#print('Path to You: ',pyou)