for a in range(1, 999):
    for b in range(1, 1000 - a):
        c = 1000 - a - b;
        if (pow(a, 2) + pow(b,2) == pow(c,2)):
            print a*b*c