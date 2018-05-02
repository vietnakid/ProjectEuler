from num2words import num2words

sum = 0
for i in range (1, 1001):
    s = num2words(i)
    for l in s:
       if l >= 'a' and l <= 'z':
           sum += 1
print sum