numTest = int(1e6) + 1
numLists = []
primes = []
setPrimes = set()

for i in range(numTest):
    numLists.append(True)

for i in range(2, numTest):
    if numLists[i]:
        primes.append(i)
        setPrimes.add(i)
        j = i * i
        while (j < numTest):
            numLists[j] = False
            j += i

print 'Done sieve step !'

res = set()

def check(x):
    for i in range(1, len(str(x))):
        if int(str(x)[-i:]) not in setPrimes:
            return False
    return True

def cal(x):
    for i in range(4): # 2 3 5 7
        y = int(str(x) + str(primes[i]))
        if (y in setPrimes and check(y)):
            res.add(y)

    for i in range(10):
        y = int(str(x) + str(i))
        if (y in setPrimes):
            cal(y)

for i in range(4):
    x = primes[i] # 2 3 5 7
    cal(x)

print sum(res)