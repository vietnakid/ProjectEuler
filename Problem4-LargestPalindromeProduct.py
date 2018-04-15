def palindrome(x):
    s = str(x);
    l = len(s) - 1;
    for i in range(0, len(s) - 1):
        if (s[i] != s[l-i]):
            return False
    return True

res = 0
for a in range(100, 999):
    for b in range(100, 999):
        if palindrome(a*b):
            res = max(res, a*b)
print res