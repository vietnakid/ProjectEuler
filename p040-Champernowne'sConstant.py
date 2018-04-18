numtest = 1e6 + 1
num = 1
s = "-"
while (len(s) < numtest):
    s += str(num)
    num += 1

print s[1], s[10], s[100], s[1000], s[10000], s[100000], s[1000000]
print int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])