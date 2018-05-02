w, h = 21, 21
arr = [[0 for x in range(w)] for y in range(h)]
arr[0][0] = 1

dx = [0, 1]
dy = [1, 0]

for i in range(w):
    for j in range(h):
        for k in range(2):
            x = i + dx[k]
            y = j + dy[k]
            if (x < h and y < w):
                arr[x][y] += arr[i][j]
print arr[20][20]
