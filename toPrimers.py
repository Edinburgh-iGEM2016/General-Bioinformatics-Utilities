def readIn(filepath):
    with open(filepath) as f:
        text = f.readlines()
    f.close()
    return text

def complement(sequence):
    return map(switch, sequence)

def switch(bp):
    if bp == 'A':
        return 'T'
    elif bp == 'T':
        return 'A'
    elif bp == 'C':
        return 'G'
    elif bp == 'G':
        return 'C'

def toForward(tup):
    forward = ''.join(tup[1][:len(tup[1])-4])
    return (tup[0] + ' forward', forward)

def toReverse(tup):
    reverse = ''.join(complement(tup[1][4:]))[::-1]
    return (tup[0] + ' reverse', reverse)

text = readIn("/home/freddie/Downloads/maryBricks")
print text

titles = [x[:len(x)-1] for x in text if x[0] == '>']
seqs = [x[:len(x)-1] for x in text if x[0] != '>']

tups = zip(titles, seqs)

print tups

f = map(toForward, tups)
r = map(toReverse, tups)

print f
print r

primers = open("/home/freddie/PycharmProjects/iGEM/mary primers", "rw+")
primers.truncate()
for x in xrange(len(f)):
    primers.write("%s\n" % str(f[x][0]))
    primers.write("%s\n" % str(f[x][1]))
    primers.write("%s\n" % str(r[x][0]))
    primers.write("%s\n" % str(r[x][1]))
primers.close()