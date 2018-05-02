f1 = 1
f2 = 0
f3 = 0
index = 0
while (len(str(f3)) < 1000):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    index += 1

print f3, index