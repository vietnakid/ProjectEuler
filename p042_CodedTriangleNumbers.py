import math

res = 0

with open("p042_words.txt") as f:
    s = f.next()
    s = s.split(",")
    for words in s:
        word = words[1:-1]
        value = 0
        for c in word:
            value += ord(c) - ord('A') + 1
        value *= 2
        sqrtValue = math.floor(math.sqrt(value))
        if (value == sqrtValue*(sqrtValue+1)):
            res += 1

print res