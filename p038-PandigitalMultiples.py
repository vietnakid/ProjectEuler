def check(n):
    s = ""
    i = 0
    while (len(s) < 9):
        i += 1
        s += str(i*n)
    if len(set(s)) == 9 and len(s) == 9 and '0' not in set(s):
        print s, n
        return s


res = ""

for i in range(9, 10000):
    res = max(res, check(i))

print res