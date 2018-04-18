factorials = [1]

for i in range(1, 10):
    factorials.append(factorials[i-1]*i)


res = 0

for i in range(10, 100000):
    x = str(i)
    sum = 0
    for c in x:
        c = ord(c) - ord('0')
        sum += factorials[c]
    if sum == i:
        res += i

print res