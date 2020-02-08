
w = 25
h = 6

#dinp = "123456789012"

f = open("input8.txt", "r")
dinp = f.read()
f.close()

layers = []
c = 0
pmin = 99999
minlayer = 999
while len(dinp) >= (w*h):
    nl = dinp[:(w*h)]
    p = nl.count('0')
    if p < pmin:
        pmin = p
        minlayer = c
    fl = []
    while len(nl) >= w:
        nline = nl[:w]
        fl.append(nline)
        nl = nl[w:]
    layers.append(fl)
    dinp = dinp[(w*h):]
    c = c + 1

flattened = []
for n in range(h):
    fl = ''
    for y in range(w):
        for x in range(len(layers)):
            #print(layers[x][n])
            if int(layers[x][n][y]) < 2:
                fl = fl + str(layers[x][n][y])
                break
    flattened.append(fl)


for g in range(len(flattened)):
    print(flattened[g])

