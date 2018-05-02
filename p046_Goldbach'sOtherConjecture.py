import math

def isPerfectSquare(x):
    if x < 0:
        return False
    sqrtX = int(round(math.sqrt(x)))
    if (sqrtX * sqrtX == x):
        return True
    return False

numTest = int(round(1e6+1))
numLists = []

for i in range(numTest):
    numLists.append(True)

primes = set()

for i in range(2, numTest):
    if numLists[i]:
        primes.add(i)
        j = i * i
        while j < numTest:
            numLists[j] = False
            j += i


for i in range(3, numTest, 2):
    check = False
    for prime in primes:
        if (i - prime) % 2 == 0:
            if isPerfectSquare((i - prime) / 2):
                check = True
                break
    if not check:
        print i
        break