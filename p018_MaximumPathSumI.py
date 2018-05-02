numLine = 15
arr = []

with open("p018_triangle.txt") as f:
    for i in range(numLine):
        arr.append([int(x) for x in next(f).split()])

f = []
for i in range(numLine):
    f.append([0 for x in range(i+1)])

f[0][0] = arr[0][0]
for i in range(1, numLine):
    f[i][0] = f[i - 1][0] + arr[i][0]
    f[i][i] = f[i-1][i-1] + arr[i][i]
    for j in range(1, i):
        f[i][j] = max(f[i-1][j], f[i-1][j-1]) + arr[i][j]

print max(f[numLine - 1])