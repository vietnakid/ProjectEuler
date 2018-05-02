def isPermu(a, b):
    a = str(a)
    b = str(b)
    if (len(a) != len(b)):
        return False
    seta = {}
    for x in a:
        if (x not in seta):
            seta[x] = 0
        else:
            seta[x] += 1
    setb = {}
    for x in b:
        if (x not in setb):
            setb[x] = 0
        else:
            setb[x] += 1
    return seta == setb

for i in range(1, 1000001):
    if (isPermu(i, 2*i) and isPermu(i, 3*i) and isPermu(i, 4*i) and isPermu(i, 5*i) and isPermu(i, 6*i)):
        print i
        break