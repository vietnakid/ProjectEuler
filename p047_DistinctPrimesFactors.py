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
    index = 0
    count = 0
    while primes[index] <= n:
        if n % primes[index] == 0:
            count += 1
            while n % primes[index] == 0:
                n /= primes[index]
        index += 1

    return count


contain4DivosorsNumber = set()

i = 4
while True:
    if analysis(i) == 4:
        contain4DivosorsNumber.add(i)
        if (i-1) in contain4DivosorsNumber and (i-2) in contain4DivosorsNumber and (i-3) in contain4DivosorsNumber:
            print i-3, i-2, i-1, i
            break
    i += 1
