arr = [0, 2, 1]
for i in xrange(1, 1000/3 + 1):
    arr.append(2*i)
    arr.append(1)
    arr.append(1)

numerator = 1
demurator = arr[100]

for i in xrange(99, 0, -1):
    numerator = demurator*arr[i] + numerator
    tmp = numerator
    numerator = demurator
    demurator = tmp

final = demurator # after swap
res = 0
while final > 0:
    res += final % 10
    final /= 10

print res