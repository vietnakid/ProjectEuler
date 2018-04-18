sum = 1
i = 3
for i in range(2, 1002, 2):
    x = i * i
    for j in range(4):
        sum += x - (j * (i-1))

print sum