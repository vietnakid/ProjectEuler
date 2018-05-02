import numpy as np

arr = []
with open("p099_base_exp.txt") as f:
    for i in range(1000):
        s = f.next()
        b = [int(x) for x in s.split(',')]
        # log(a^b) = b*log(a)
        arr.append(b[1]*np.log(b[0]))

res = 0
maxx = 0
for i in range(1000):
    if arr[i] > maxx:
        maxx = arr[i]
        res = i

print res + 1
