numTest = int(1e6 + 1)
primes = []

for i in range(numTest):
    primes.append(True)

for i in range(2, numTest):
    if primes[i]:
        j = i * i
        while (j < numTest):
            primes[j] = False
            j += i

def check(x):
    leng = len(str(x))
    for i in range(leng):
        x = x + pow(10, leng)*(x%10)
        x /= 10
        if (primes[x] == False):
            return False
    return True

count = 0
for i in range(2, numTest):
    if check(i):
        count += 1

print count