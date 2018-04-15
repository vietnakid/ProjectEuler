def sumSquare(n):
    sum = 0
    for i in range(1, n+1):
        sum += pow(i, 2)
    return sum

def squareSum(n):
    sum = n*(n+1) / 2
    return pow(sum, 2)

print abs(sumSquare(100) - squareSum(100))