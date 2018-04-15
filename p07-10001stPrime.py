resIndex = 10001
numTest = resIndex * 20
numLists = []

for i in range(numTest):
    numLists.append(True)

count = 0
for i in range(2, numTest):
    if numLists[i]:
        count += 1
        if (resIndex == count):
            print i, count
        j = i * i
        while (j < numTest):
            numLists[j] = False
            j += i
