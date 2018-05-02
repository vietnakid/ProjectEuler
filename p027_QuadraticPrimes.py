numTest = int(2e6 + 1)
primes = []

for i in range(numTest):
    primes.append(True)

for i in range(2, numTest):
    if primes[i]:
        j = i * i
        while (j < numTest):
            primes[j] = False
            j += i

maxx = 0
res = 0
for i in range(-1000, 1001):
    for j in range(-1000, 1001):
        n = 0
        while (primes[n*n + i*n + j]):
            n += 1
        if (n > maxx):
            maxx = n
            res = i*j
print res