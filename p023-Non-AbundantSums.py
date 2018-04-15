import math

def sumOfFactor(n):
    if n == 1:
        return 0
    sum = 0
    sqrtN = int(round(math.sqrt(n)))
    for i in range(1, sqrtN+1):
        if n % i == 0:
            sum += i
            sum += n / i
    if (math.sqrt(n) == sqrtN):
        sum -= sqrtN
    sum -= n
    return sum

abundants = []
upperBound = 28123 + 1

for i in range(1, upperBound):
    if (sumOfFactor(i) > i):
        abundants.append(i)

lengAbundants = len(abundants)
sum = 0
canConstruct = set()
for i in range(lengAbundants):
    for j in range(lengAbundants):
        canConstruct.add(abundants[i] + abundants[j])

for i in range(1, upperBound):
    if i not in canConstruct:
        sum += i
print sum