ckn = [[0 for x in range(101) ] for x in range (101)]
res = 0

ckn[0][0] = 1
for i in range(1, 101):
    ckn[i][0] = 1
    ckn[i][i] = 1
    for j in range(1, i+1):
        ckn[i][j] = ckn[i-1][j] + ckn[i-1][j-1]
        if ckn[i][j] > 1000000:
            res += 1

print res