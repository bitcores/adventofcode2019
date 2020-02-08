
def modecode(dim):
    optcode = dim % 100
    dim = dim // 100
    c = dim % 10
    dim = dim // 10
    b = dim % 10
    dim = dim // 10
    a = dim % 10
    return([optcode, a, b, c])


#dinp = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
f = open("input7.txt", "r")
dinp = f.read()
f.close()

list = dinp.split(",")

class intcomp():
    def __init__(self, n, list):
        self.init = 1
        self.state = 0
        self.list = list.copy()
        self.inc = 0
        self.pos = 0
        self.output = 0
        #print("Intcode Amplifier",n+1,"Initialized")

    def runcomp(self, in1=-1, in2=0):
        self.state = 1
        while self.state == 1:
            mc = modecode(int(self.list[self.pos]))

            if mc[0] == 99:
                self.state = 99
                break

            x = int(self.list[self.pos+1])
            if mc[3] == 0:
                vx = int(self.list[x])
            elif mc[3] == 1:
                vx = x
            if mc[0] == 1 or mc[0] == 2 or mc[0] == 7 or mc[0] == 8:
                y = int(self.list[self.pos+2])
                if mc[2] == 0:
                    vy = int(self.list[y])
                elif mc[2] == 1:
                    vy = y
                o = int(self.list[self.pos+3])
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
            elif mc[0] == 3 or mc[0] == 4:
                if mc[0] == 3:
                    vin = 0
                    if self.inc < 1 and in1 < 0:
                        vin = input("input integer: ")
                    elif self.inc < 1 and in1 >= 0:
                        vin = in1
                    else:
                        vin = in2
                    #print("input:", vin)
                    self.list[x] = int(vin)
                    self.inc = self.inc + 1
                elif mc[0] == 4:
                    #print(vx)
                    self.state = 2             
                    self.output = vx
                self.pos = self.pos + 2
                
            elif mc[0] == 5 or mc[0] == 6:
                y = int(self.list[self.pos+2])
                if mc[2] == 0:
                    vy = int(self.list[y])
                elif mc[2] == 1:
                    vy = y
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

## this is hilariously incomprehensible and I wasted too much time on it
highout = 0
values = [5,5,5,5,5]
highvals = []

for z in range(5,10):
    values[0] = z
    for y in range(5,10):
        values[1] = y
        for x in range(5,10):
            values[2] = x
            for w in range(5,10):
                values[3] = w
                for v in range(5,10):
                    values[4] = v
                    if values.count(5) == 1 and values.count(6) == 1 and values.count(7) == 1 and values.count(8) == 1 and values.count(9) == 1:
                        out = 0
                        states = [0,0,0,0,0]
                        amps = []
                        for n in range(5):
                            amps.append(intcomp(n,list))
                        while states[4] != 99:
                            for m in range(5):
                                amps[m].runcomp(values[m],out)
                                out = amps[m].output
                                states[m] = amps[m].state
                                if out > highout:
                                    highout = out
                                    highvals = values[:]
    

print("Amplification complete")
print(highout)
print(highvals)