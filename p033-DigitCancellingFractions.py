def simplyfy(a, b):
    if (a % 10 == 0 or b % 10 == 0):
        return False
    x = str(a)
    y = str(b)
    if (x[0] == y[0] and x[1] < y[1] and float(x[1])/float(y[1]) == float(a)/float(b)):
        return True
    if (x[1] == y[0] and x[0] < y[1] and float(x[0])/float(y[1]) == float(a)/float(b)):
        return True
    if (x[0] == y[1] and x[1] < y[0] and float(x[1])/float(y[0]) == float(a)/float(b)):
        return True
    if (x[1] == y[1] and x[0] < y[0] and float(x[0])/float(y[0]) == float(a)/float(b)):
        return True
    return False

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

denominator = 1
numerator = 1
for i in range(10, 100):
    for j in range(10, 100):
        if (simplyfy(i, j)):
            numerator *= i
            denominator *= j

print numerator, denominator
print denominator / gcd(numerator, denominator)