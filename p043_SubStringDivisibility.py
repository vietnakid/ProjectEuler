import itertools

arr = [x for x in itertools.permutations(range(10))]

sum = 0

def fromArraytoNumber(rawArray):
    value = 0
    for x in rawArray:
        value = value * 10 + x
    return value

for it in arr:
    d2 = fromArraytoNumber(it[1:4])
    d3 = fromArraytoNumber(it[2:5])
    d5 = fromArraytoNumber(it[3:6])
    d7 = fromArraytoNumber(it[4:7])
    d11 = fromArraytoNumber(it[5:8])
    d13 = fromArraytoNumber(it[6:9])
    d17 = fromArraytoNumber(it[7:10])
    if (d2 % 2 == 0 and d3 % 3 == 0 and d5 % 5 == 0 and d7 % 7 == 0 and d11 % 11 == 0 and d13 % 13 == 0 and d17 % 17 == 0):
        sum += fromArraytoNumber(it)

print sum