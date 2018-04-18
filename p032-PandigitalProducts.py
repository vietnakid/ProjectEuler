import itertools

arr = [x for x in itertools.permutations(range(1, 10))]

res = set()

for permutation in arr:
    x1 = 0
    for i in range(1, 7):
        x1 = x1 * 10 + permutation[i-1]
        x2 = 0
        x3 = 0
        for ii in range(i, 9):
            x3 = x3 * 10 + permutation[ii]

        for j in range(i+1, 8):
            x2 = x2 * 10 + permutation[j-1]
            x3 %= pow(10,9-j)
            if (x1 * x2 == x3):
                res.add(x3)
            if (x1 * x2 > x3):
                break

print sum(res)