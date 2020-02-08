import operator
from ordered_set import OrderedSet

def idroid(co, n):
    name = chr(65+co) + str(n)
    return name

roidsdict = {}
visdict = {}
ix = 0
iy = 0
w = 0
h = 0
#with open("input10test.txt") as fp:
with open("input10.txt") as fp:
    for line in fp:
        w = len(line)
        ix = 0
        for p in line:
            if p == "#":
                roidname = idroid(iy, ix)
                roidsdict[roidname] = [ix, iy]
            ix = ix + 1 
        iy = iy + 1
h = iy

#print(roidsdict)
slopesdict = {}
for roid in roidsdict:
    ddict = set()
    for comp in roidsdict:
        if comp != roid:
            sx = roidsdict[roid][0]
            sy = roidsdict[roid][1]
            tx = roidsdict[comp][0]
            ty = roidsdict[comp][1]

            if sx == tx:
                #vertical line
                slope = 99999999
                if sy > ty:
                    slope = slope * -1
                    slope = 'N' + str(slope)
                else:
                    slope = 'S' + str(slope)
            elif sy == ty:
                #horizontal line
                slope = 0.000001
                if sx > tx:
                    slope = slope * -1
                    slope = 'N' + str(slope)
                else:
                    slope = 'S' + str(slope)
            else:
                slope = (ty - sy) / (tx - sx)
                if sy > ty:
                    slope = 'N' + str(slope)
                else:
                    slope = 'S' + str(slope)


            ddict.add(slope)
    slopesdict[roid] = len(ddict)

dmax = (max(slopesdict.items(), key=operator.itemgetter(1))[0])
print(slopesdict[dmax])
print(dmax, roidsdict[dmax])

## ============= Part 2 code
slodict = {}
slodict[1] = {}
slodict[2] = {}
slodict[3] = {}
slodict[4] = {}
for comp in roidsdict:
    if comp != dmax:
        sx = roidsdict[dmax][0]
        sy = roidsdict[dmax][1]
        tx = roidsdict[comp][0]
        ty = roidsdict[comp][1]

        if sx == tx:
            #vertical line
            slope = 99999999
            if sy > ty:
                #q1
                slope = slope * -1
                slodict[1][comp] = slope
            else:
                #q2
                slodict[2][comp] = slope
        elif sy == ty:
            #horizontal line
            slope = 0.000001
            if sx > tx:
                #q3
                slope = slope * -1
                slodict[3][comp] = slope
            else:
                #q2
                slodict[2][comp] = slope
        else:
            slope = (ty - sy) / (tx - sx)
            if sy > ty:
                if slope > 0:
                    #q4
                    slodict[4][comp] = slope
                else:
                    #q1
                    slodict[1][comp] = slope

            else:
                if slope > 0:
                    #2
                    slodict[2][comp] = slope
                else:
                    #q3
                    slodict[3][comp] = slope

sslodict = {}
sslodict[1] = {}
sslodict[2] = {}
sslodict[3] = {}
sslodict[4] = {}
for x in range(1,5):
    for key, value in sorted(slodict[x].items(), key=lambda item: item[1]):
        sslodict[x][key] = value

desroids = OrderedSet()

while len(sslodict[1]) > 0 or len(sslodict[2]) > 0 or len(sslodict[3]) > 0 or len(sslodict[4]) > 0:
    for y in range(1,5):
        if len(sslodict[y]) > 0:
            tmpdes = OrderedSet()
            testroid = next(iter(sslodict[y]))
            for p in sslodict[y]:
                samedict = [i for i,j in sslodict[y].items() if j == sslodict[y][p]]
                if y == 1 or y == 4:
                    tmpdes.add(samedict[-1:][0])
                else:
                    tmpdes.add(samedict[:1][0])
                testroid = p

            for d in tmpdes:
                sslodict[y].pop(d)
                desroids.add(d)


print(desroids)
print(roidsdict[desroids[199]])
print(roidsdict[desroids[199]][0] * 100 + roidsdict[desroids[199]][1])

