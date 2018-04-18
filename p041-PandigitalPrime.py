def pandigital(x):
    leng = len(str(x))
    check = []
    for i in range(10):
        check.append(False)

    for c in str(x):
        check[ord(c) - ord('0')] = True

    for i in range(1, leng+1):
        if check[i] == False:
            return False
    return True

numTest = int(7e7 + 1)
primes = []

for i in range(numTest):
    primes.append(True)

res = 0
for i in range(2, numTest):
    if primes[i]:
        if (pandigital(i)):
            res = i
        j = i * i
        while (j < numTest):
            primes[j] = False
            j += i

print res