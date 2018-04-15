with open("p022_names.txt") as f:
    s = f.next()
    s = s.split(",")
    index = 0
    sum = 0
    s.sort()
    for words in s:
        index += 1
        word = words[1:-1]
        s = 0
        for letter in word:
            s += ord(letter) - ord('A') + 1

        s *= index
        sum += s

    print sum
