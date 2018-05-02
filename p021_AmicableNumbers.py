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

sum = 0
arr = [sumOfFactor(x) for x in range(10001)]
for i in range(1, 10001):
    x = arr[i]
    if (x <= 10000 and arr[x] == i and x > i):
        sum += x + i
print sum
