import itertools

arr = [x for x in itertools.permutations(range(10))]
res = arr[1000000-1]
s = ""
for x in res:
    s += str(x)
print(s)