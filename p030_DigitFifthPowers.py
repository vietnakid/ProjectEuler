def isSum(x):
    sum = 0
    for c in str(x):
        sum += pow(ord(c) - ord('0'), 5)
    return sum == x


res = 0

for i in range(2, 1000000):
    if isSum(i):
        res += i

print res