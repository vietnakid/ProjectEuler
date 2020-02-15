map = {}
res = {}

for i in xrange(100000):
    x = str(i*i*i)
    arr = [0 for j in xrange(10)]

    for c in x:
        arr[ord(c) - ord('0')] += 1
    s = ""
    for a in arr:
        s += chr(a + ord('0'))
    if s not in map:
        map[s] = 1
        res[s] = x
    else:
        map[s] += 1
    if map[s] == 5:
        print res[s]
        break
