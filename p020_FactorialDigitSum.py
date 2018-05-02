def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

fac100 = str(factorial(100))
res = 0
for x in fac100:
    res += int(x)

print res