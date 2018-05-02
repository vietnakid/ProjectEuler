arr = []
with open("p081_matrix.txt", 'r') as f:
    for i in range(80):
        s = f.next()
        s = s.split(',')
        for j in range(80):
            s[j] = int(s[j])
        arr.append(s)

f = [[0 for k in range (80)] for x in range(80)]

f[0][0] = arr[0][0]
for i in range(1, 80):
    f[i][0] = f[i-1][0] + arr[i][0]
    f[0][i] = f[0][i-1] + arr[0][i]

for i in range(1, 80):
    for j in range(1, 80):
        f[i][j] = min(f[i-1][j], f[i][j-1]) + arr[i][j]

print f[i][j]
