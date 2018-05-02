res = 0

for i in range(1, 1001):
    x = pow(i, i)
    res += int(str(x)[-10:])
    res = int(str(res)[-10:])

print res