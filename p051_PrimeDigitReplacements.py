numTest = int(1e6)
numLists = [True for x in xrange(numTest)]
primes = []

for i in xrange(2, numTest):
    if numLists[i]:
        primes.append(i)
        j = i * i
        while (j < numTest):
            numLists[j] = False
            j += i

print 'Done sieve step !'

primes = sorted(primes)

for x in primes:
    x = str(x)
    for i in xrange(1, pow(2, len(x) - 1)):
        permu = str(bin(i))[2:]
        while len(permu) < len(x) - 1:
            permu = '0' + permu
        permu += '0' # end with 1 3 5 7 9
        check = True
        numCheck = -1
        for j in xrange(len(x)):
            if permu[j] == '1':
                if numCheck == -1:
                    numCheck = x[j]
                if x[j] > '2' or x[j] != numCheck:
                    check = False
                    break
        if check == False:
            continue

        count = 0
        for j in xrange(10):
            num = ""
            for ii in xrange(len(permu)):
                if permu[ii] == '1':
                    num += chr(j + ord('0'))
                else:
                    num += x[ii]
            xx = int(num)
            if xx in primes:
                count += 1
        if (count == 8):
            print "founded!"
            print x, permu, count
            break
        print x, permu, count