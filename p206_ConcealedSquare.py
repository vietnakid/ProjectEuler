def match(n):
    s = str(n)
    return not all(int(s[x*2]) == x+1 for x in xrange(9))

n = 138902663    # sqrt(19293949596979899)
while match(n*n):
    m = str(n)
    if (m[len(m) - 1] == '3'):
        n -= 6
    else:
        n -= 4

print n*10    #add the trailing zero