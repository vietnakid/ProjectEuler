import math

def sumOfFactor(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

sum = 0
arr = [sumOfFactor(x) for x in range(10001)]
print arr
for i in range(1, 10001):
    x = arr[i]
    if (x <= 10000 and arr[x] == i and x > i):
        sum += x + i
print sum
