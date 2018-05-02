def findLeng(x):
    appear = {}
    index = 0
    a = 1
    while (a != 0):
        index += 1
        a %= x
        if a in appear:
            return index - appear[a]
        appear[a] = index
        a *= 10
    return 0

res = 0
maxx = 0
for i in range(2, 1001):
    if (findLeng(i) > maxx):
        maxx = findLeng(i)
        res = i

print res