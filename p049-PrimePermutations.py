import itertools

numTest = int(1e4)
numLists = []
primes = []

for i in range(numTest):
    numLists.append(True)

for i in range(2, numTest):
    if numLists[i]:
        if (i > 1000):
            primes.append(i)
        j = i * i
        while (j < numTest):
            numLists[j] = False
            j += i

print 'Done sieve step !'

def toInt(arr):
    x = 0
    for a in arr:
        x = x*10 + int(a)
    return x


def checkPermutaion(a, b, c):
    arr = [toInt(x) for x in itertools.permutations(list(str(a)))]
    if (b not in arr or c not in arr):
        return False
    return True


length = len(primes)

for i in range(length):
    x = primes[i]
    for j in range(i+1, length):
        y = primes[j]
        if ((x + y) % 2 == 0):
            z = (y + x) / 2
            if z in primes:
                if checkPermutaion(x, y, z):
                    print x, z, y