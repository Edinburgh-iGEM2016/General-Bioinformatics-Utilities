import lexEncode

lexicon = lexEncode.encode("/home/freddie/PycharmProjects/iGEM/ogdan",
                           "/home/freddie/PycharmProjects/iGEM/codeRecord",
                           "/home/freddie/PycharmProjects/iGEM/gBlocks")

phytoIllegal = [('BsaI', 'GGTCTC'), ('BsaI Reverse', 'GAGACC')]
phytoAvoid = [('BpiI', 'GAAGAC'), ('BsmBI', 'CGTCTC'), ('BpiI Reverse', 'GTCTTC'), ('BsmBI Reverse', 'GAGACG')]
biobrickIllegal = [('EcoRI', 'GAATTC'), ('XbaI', 'TCTAGA'), ('SpeI', 'ACTAGT'), ('PstI', 'CTGCAG'),
                   ('EcoRI Reverse', 'GAATTC'), ('XbaI Reverse', 'TCTAGA'), ('SpeI Reverse', 'ACTAGA'), ('PstI Reverse', 'CAGCAG')]
biobrickAvoid = [('NotI', 'GCGGCCGC'), ('NotI Reverse', 'GCGGCCGC')]

allBadThings = phytoAvoid + phytoIllegal + biobrickIllegal + biobrickAvoid

def checkProhibited(toCheck, prohibited):
    naughtyList = [(eachEvil[0], eachEvil[1], toCheck.find(eachEvil[1])) for eachEvil in prohibited]
    return filter(lambda x: x[2] != -1, naughtyList)

restrictionsPerWord = [(word[0], checkProhibited(word[1], allBadThings), checkProhibited(word[2], allBadThings)) for word in lexicon]
print filter(lambda x: x[1] != [] or x[2] != [], restrictionsPerWord)
print len(filter(lambda x: x[1] != [] or x[2] != [], restrictionsPerWord))
