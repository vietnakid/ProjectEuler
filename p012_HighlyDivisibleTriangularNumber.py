import math

def numberOfFactor(n):
    p = n * (n + 1) / 2
    count = 0
    for i in range(1, int(math.sqrt(p) + 1)):
        if (p % i == 0):
            count += 2
    print n, p, count
    return count

n = 1
while True:

    if (numberOfFactor(n) > 500):
        break
    n += 1