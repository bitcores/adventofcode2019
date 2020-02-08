
# range 271973-785961
def movenxtvalid(sp):
    for x in range(0,5):
        if sp[x] > sp[x+1]:
            for y in range(5,x,-1):
                sp[y] = sp[x]
    return sp

def incrnum(sp):

    return True

def checkasc(sp):
    for x in range(0,5):
        if sp[x] > sp[x+1]:
            return False
    return True

def checkpair(sp):
    for x in range(0,5):
        if sp[x] == sp[x+1]:
            if (x > 0 and sp[x-1] != sp[x]) or x == 0:
                if x < 4 and sp[x+2] != sp[x]:
                    return True
                elif x == 4:
                    return True
    return False

def joinnum(num):
    num.reverse()
    out = 0
    for x in range(0,6):
        out = out + num[x]*10**x
    return out

def splitnum(num):
    split = []
    for x in range(0,6):
        split.append(num % 10)
        num = num // 10
    split.reverse()
    return split

#n = 333333
# 271973, 785961
# 111111, 123456
validnums = 0
for n in range(271973, 785961):
    spnum = splitnum(n)
#while joinnum(spnum) < 333348:
    #spnum = movenxtvalid(spnum)

    if checkasc(spnum) and checkpair(spnum):
        validnums = validnums + 1
        print(joinnum(spnum))

print(validnums)
    
