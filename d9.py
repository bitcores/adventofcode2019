import time

def modecode(dim):
    optcode = dim % 100
    dim = dim // 100
    c = dim % 10
    dim = dim // 10
    b = dim % 10
    dim = dim // 10
    a = dim % 10
    return([optcode, a, b, c])

# 1 add
# 2 multiply
# 3 input
# 4 output
# 5 move cursor if not 0
# 6 move cursor if 0
# 7 set 1 if x < y
# 8 set 1 if x == y
# 9 set relative base offset

st = time.time()

dinp = "3,1,109,583,108,0,1,9,1106,-1,14,4,1,99,107,0,1,19,1105,-1,27,104,-1,102,-1,1,1,21101,0,38,0,20101,0,1,1,1105,1,138,2101,1,1,41,101,596,41,45,1101,1,596,77,1101,0,1,53,101,1,77,77,101,1,53,53,7,45,77,67,1105,-1,128,108,1,1,74,1105,-1,128,1005,-1,54,1,53,77,93,7,45,93,88,1105,-1,101,1101,0,1,-1,1,53,93,93,1105,1,83,21101,0,116,0,20101,0,1,1,20101,0,53,2,1105,1,235,1205,2,54,4,53,2101,0,1,1,1105,1,101,108,1,1,133,1105,-1,137,4,1,99,22101,0,1,2,22101,0,1,1,21101,0,163,3,22101,0,1,4,22101,0,2,5,109,3,1105,1,198,109,-3,22102,-1,1,1,22201,1,4,3,22102,-1,1,1,1208,3,0,182,2105,-1,0,1208,3,1,189,2105,-1,0,22101,0,4,1,1105,1,146,1207,1,1,203,2105,-1,0,21101,0,222,3,22101,0,2,4,22101,0,1,5,109,3,1105,1,235,109,-3,22201,1,4,1,21101,0,2,2,1105,1,235,1105,0,280,101,383,236,243,1107,-1,583,247,1106,-1,276,101,383,236,256,102,1,275,-1,102,2,275,275,1007,275,0,266,1105,-1,280,101,1,236,236,1105,1,238,1,101,-1,236,236,101,383,236,286,207,1,-1,289,1106,-1,-1,22101,0,1,3,2102,1,2,363,2102,-1,2,369,22102,0,1,1,22102,0,2,2,101,1,236,320,101,-1,320,320,1107,-1,0,324,2105,-1,0,22102,2,2,2,101,383,320,336,207,3,-1,339,1105,-1,361,22101,1,2,2,22102,-1,3,3,101,383,320,354,22001,-1,3,3,22102,-1,3,3,1207,2,-1,366,1105,-1,315,22101,-1,2,2,101,383,320,377,22001,-1,1,1,1105,1,315"
#f = open("input9.txt", "r")
#dinp = f.read()
#f.close()

list = dinp.split(",")

class intcomp():
    def xmem(self):
        # make the program memory x times larger
        xp = len(self.list) * 10000
        for x in range(xp):
            self.list.append(0)

    def __init__(self, n, list):
        self.init = 1
        self.state = 0
        self.list = list.copy()
        self.inc = 0
        self.pos = 0
        self.output = 0
        self.relbase = 0

    def runcomp(self, in1=-1, in2=0):
        self.state = 1
        while self.state == 1:
            mc = modecode(int(self.list[self.pos]))
            #print(self.pos, mc[0])

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
                if mc[1] == 2:
                    o = self.relbase+o

                if mc[0] == 1:
                    self.list[o] = vx + vy

                elif mc[0] == 2:
                    self.list[o] = vx * vy

                elif mc[0] == 7:
                    if vx < vy:
                        self.list[o] = 1
                    else:
                        self.list[o] = 0

                elif mc[0] == 8:
                    if vx == vy:
                        self.list[o] = 1
                    else:
                        self.list[o] = 0

                self.pos = self.pos + 4

            elif mc[0] == 3 or mc[0] == 4 or mc[0] == 9:
                if mc[0] == 3:
                    # mode 3 acts like intermediate mode by default
                    vx = x
                    if mc[3] == 2:
                        vx = self.relbase+x
                    vin = 0
                    if self.inc < 1 and in1 < 0:
                        vin = input("input integer: ")
                    elif self.inc < 1 and in1 >= 0:
                        vin = in1
                    else:
                        vin = in2
                    self.list[vx] = int(vin)
                    self.inc = self.inc + 1

                elif mc[0] == 4:
                    self.state = 2             
                    self.output = vx

                elif mc[0] == 9:          
                    self.relbase = self.relbase+vx

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

            else:
                print(self.pos)
                print(mc)
                print(self.list)
                break
            #input()

boostcomp = intcomp(0, list)
boostcomp.xmem()
while boostcomp.state != 99:
    boostcomp.runcomp(19338240)
    out = boostcomp.output
    if boostcomp.state == 2:
        print(out)

print('Intcode Computer end @ ', time.time() - st)