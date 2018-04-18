numTest = int(1e6) + 1
numLists = []
primes = []

for i in range(numTest):
    numLists.append(True)

for i in range(2, numTest):
    if numLists[i]:
        primes.append(i)
        j = i * i
        while (j < numTest):
            numLists[j] = False
            j += i

print 'Done sieve step !'

def analysis(n):
    start = -1
    end = -1
    sum = 0
    while (sum != n):
        while (sum < n):
            end += 1
            sum += primes[end]
        while (sum > n):
            start += 1
            sum -= primes[start]
    # print sum, n, start, end
    return end - start

res = 0
maxLeng = 0

for i in primes:
    leng = analysis(i)
    if (leng > maxLeng):
        maxLeng = leng
        res = i
        print res, maxLeng

print res, maxLeng