res = set()
for i in range(2, 101):
    for j in range(2, 101):
        res.add(pow(i, j))

print len(res)