count = 0
for exponent in range(1, 22):
    for base in range(1, 10):
        if len(str(pow(base, exponent))) == exponent:
            count += 1
print count
