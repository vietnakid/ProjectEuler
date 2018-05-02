def collatazLeng(n):
    leng = 0
    while (n != 1):
        leng += 1
        if (n % 2 == 0):
            n /= 2
        else:
            n = 3*n +1
    return leng+1

maxLeng = 0
maxx = 0
for i in range(1, 1000001):
    leng = collatazLeng(i)
    if leng > maxLeng:
        maxLeng = leng
        maxx = i
print maxx, maxLeng