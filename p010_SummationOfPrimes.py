numTest = int(2e6 + 1)
numLists = []

for i in range(numTest):
    numLists.append(True)

sum = 0
for i in range(2, numTest):
    if numLists[i]:
        sum += i
        j = i * i
        while (j < numTest):
            numLists[j] = False
            j += i
print sum