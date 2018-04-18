def triangle(n):
    return n*(n+1) / 2

def pentagonal(n):
    return n*(3*n - 1) / 2

def hexagonal(n):
    return n*(2*n - 1)

trin = 1
triset = set()
penn = 1
penset = set()
hexn = 1
hexset = set()

while (True):
    triNum = triangle(trin)
    penNum = pentagonal(penn)
    hexNum = hexagonal(hexn)
    minOfAll = min(triNum, penNum, hexNum)
    if triNum == minOfAll:
        triset.add(triNum)
        trin += 1
        if triNum in penset and triNum in hexset:
            print triNum
    elif penNum == minOfAll:
        penset.add(penNum)
        penn += 1
        if penNum in triset and penNum in hexset:
            print penNum
    elif hexNum == minOfAll:
        hexset.add(hexNum)
        hexn += 1
        if hexNum in triset and hexNum in penset:
            print hexNum