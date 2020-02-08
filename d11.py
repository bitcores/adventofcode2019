import copy

def modecode(dim):
    optcode = dim % 100
    dim = dim // 100
    c = dim % 10
    dim = dim // 10
    b = dim % 10
    dim = dim // 10
    a = dim % 10
    return([optcode, a, b, c])

def iname(co, n):
    name = chr(65+co) + str(n)
    return name

def setdirection(d, t):
    if t == 0:
        t = -1
    d = d + t
    if d > 3:
        d = 0
    elif d < 0:
        d = 3
    return d

def stepdirection(p, s):
    if s == 0:
        p[1] = p[1] + 1
    elif s == 1:
        p[0] = p[0] + 1
    elif s == 2:
        p[1] = p[1] - 1
    elif s == 3:
        p[0] = p[0] - 1
    return p

# 1 add
# 2 multiply
# 3 input
# 4 output
# 5 move cursor if not 0
# 6 move cursor if 0
# 7 set 1 if x < y
# 8 set 1 if x == y
# 9 set relative base offset


#dinp = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
f = open("input11.txt", "r")
dinp = f.read()
f.close()

list = dinp.split(",")

class intcomp():
    def xmem(self):
        # make the program memory x times larger
        xp = len(self.list) * 5
        for x in range(xp):
            self.list.append(0)

    def __init__(self, n, list):
        self.init = 1
        self.state = 0
        self.list = copy.deepcopy(list)
        self.inc = 0
        self.pos = 0
        self.output = 0
        self.relbase = 0
        self.debug = 0

    def runcomp(self, in1=-9999, in2=-9999):
        self.state = 1
        while self.state == 1:
            mc = modecode(int(self.list[self.pos]))
            if self.debug == 1:
                print(self.pos, mc)

            if mc[0] == 99:
                self.state = 99
                break

            x = int(self.list[self.pos+1])
            if mc[3] == 0:
                vx = int(self.list[x])
            elif mc[3] == 1:
                vx = x
            elif mc[3] == 2:
                vx = int(self.list[self.relbase+x])

            if mc[0] == 1 or mc[0] == 2 or mc[0] == 7 or mc[0] == 8:
                y = int(self.list[self.pos+2])
                if mc[2] == 0:
                    vy = int(self.list[y])
                elif mc[2] == 1:
                    vy = y
                elif mc[2] == 2:
                    vy = int(self.list[self.relbase+y])

                o = int(self.list[self.pos+3])
                if mc[1] == 0:
                    vo = o
                elif mc[1] == 2:
                    vo = self.relbase+o

                if mc[0] == 1:
                    self.list[vo] = vx + vy

                elif mc[0] == 2:
                    self.list[vo] = vx * vy

                elif mc[0] == 7:
                    if vx < vy:
                        self.list[vo] = 1
                    else:
                        self.list[vo] = 0

                elif mc[0] == 8:
                    if vx == vy:
                        self.list[vo] = 1
                    else:
                        self.list[vo] = 0

                self.pos = self.pos + 4
                if self.debug == 1:
                    print(mc[0], vx, vy, vo)

            elif mc[0] == 3 or mc[0] == 4 or mc[0] == 9:
                if mc[0] == 3:
                    # mode 3 acts like intermediate mode by default
                    vx = x
                    if mc[3] == 2:
                        vx = self.relbase+x
                    vin = 0
                    if in1 == -9999:
                        vin = input("input integer: ")
                    elif in2 != -9999:
                        vin = in2
                    else:
                        vin = in1
                    self.list[vx] = int(vin)
                    self.inc = self.inc + 1
                    if self.debug == 1:
                        print(mc[0], vx, vin)

                elif mc[0] == 4:
                    self.state = 2             
                    self.output = vx
                    if self.debug == 1:
                        print(mc[0], vx)

                elif mc[0] == 9:          
                    self.relbase = self.relbase+vx
                    if self.debug == 1:
                        print(mc[0], vx, self.relbase)

                self.pos = self.pos + 2              
                
            elif mc[0] == 5 or mc[0] == 6:
                y = int(self.list[self.pos+2])
                if mc[2] == 0:
                    vy = int(self.list[y])
                elif mc[2] == 1:
                    vy = y
                elif mc[2] == 2:
                    vy = int(self.list[self.relbase+y])

                if mc[0] == 5:
                    if vx < 0 or vx > 0:
                        self.pos = vy
                    else:
                        self.pos = self.pos + 3

                elif mc[0] == 6:
                    if vx == 0:
                        self.pos = vy
                    else:
                        self.pos = self.pos + 3
                
                if self.debug == 1:
                    print(mc[0], vx, vy)

            else:
                print("Error printing fault")
                print(self.pos)
                print(mc)
                print(self.list)
                self.state = 99
                break

            if self.debug == 1:   
                input()

# 0 up = y+1
# 1 right = x+1
# 2 down = y-1
# 3 left = x-1
# direction = 0, 1, 2, 3

direction = 0
rpos = [0,0]
inpcolor = 1
turncolor = False
paintdict = {}
xmin = 9999999
xmax = -9999999
ymin = 9999999
ymax = -9999999

boostcomp = intcomp(0, list)
boostcomp.xmem()
while boostcomp.state != 99:
    boostcomp.runcomp(inpcolor)
    out = boostcomp.output
    
    if boostcomp.state == 2:
        if turncolor == False:
            paintdict[iname(rpos[0],rpos[1])] = out
            
        else:
            direction = setdirection(direction, out)
            rpos = stepdirection(rpos, direction)

            if rpos[0] < xmin:
                xmin = rpos[0]
            elif rpos[0] > xmax:
                xmax = rpos[0]
            
            if rpos[1] < ymin:
                ymin = rpos[1]
            elif rpos[1] > ymax:
                ymax = rpos[1]

            if iname(rpos[0],rpos[1]) in paintdict:
                inpcolor = paintdict[iname(rpos[0],rpos[1])]
            else:
                inpcolor = 0
            
        turncolor = not turncolor

print("Number of panels painted at least once: ",len(paintdict))
print("Registration identifier")
for y in range(ymax, ymin-1, -1):
    outline = ''
    for x in range(xmin, xmax+1):    
        if iname(x,y) in paintdict:
            p = paintdict[iname(x,y)]
            if p == 1:
                outline = outline + '#'
            else:
                outline = outline + ' '
        else:
                outline = outline + ' '
    print(outline)