numTest = int(1e6 + 1)

def palindrome(x):
    s = str(x);
    l = len(s) - 1;
    for i in range(0, len(s) - 1):
        if (s[i] != s[l-i]):
            return False
    return True

res = 0
for i in range (numTest):
    x = "{0:b}".format(i)
    if (palindrome(i) and palindrome(x)):
        res += i

print res