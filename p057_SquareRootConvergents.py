res = 0
for i in range(1, 1001):
    numerate = 1
    denominator = 2
    for j in range(1, i):
        numerate += 2*denominator
        tmp = numerate
        numerate = denominator
        denominator = tmp
    numerate += denominator
    if len(str(numerate)) > len(str(denominator)):
        res += 1

print res