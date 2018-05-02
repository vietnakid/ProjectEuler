import math

def pentagonal(n):
    return n*(3*n -1)/2

def isPentagonal(number):
    penTest = (math.sqrt(1 + 24 * number) + 1.0) / 6.0
    return penTest == int(penTest)

i = 1
notFound = True
while notFound:
    i += 1
    for j in range(1, i):
        x = pentagonal(i)
        y = pentagonal(j)
        if isPentagonal(x+y) and isPentagonal(x-y):
            print x-y
            notFound = False