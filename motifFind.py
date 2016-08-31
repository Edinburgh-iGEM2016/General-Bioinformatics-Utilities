
def getWords(sentenceSeq):
    formCounter = 0
    words = []
    while True:
        if formCounter % 2 == 0:
            wordPos = findSplicedMotif(sentenceSeq, "GGAGNCCNNNNTAGCTAATCACTTATGANNGGNNTTNNGGNNTTNNCGCT")
        else:
            wordPos = findSplicedMotif(sentenceSeq, "CGCTNCCNNNNTAGCTAATCACTTATGANNGGNNTTNNGGNNTTNNGGAG")
        if wordPos == False:
            break
        formCounter = formCounter + 1
        words.append(sentenceSeq[:wordPos[len(wordPos) - 1] + 1])
        sentenceSeq = sentenceSeq[wordPos[len(wordPos) - 4]:]
        print words
    return words

def findSplicedMotif(toSearch, subsequence):
    basePositions = {}
    for eachBase in ['A', 'T', 'C', 'G']:
        basePositions[eachBase] = [index for (index, base) in enumerate(toSearch) if base == eachBase]
    basePositions['N'] = range(len(toSearch))
    position = []
    currentPosition = -1
    for eachBase in subsequence:
        try:
            currentPosition = min(filter(lambda x: x > currentPosition, basePositions[eachBase]))
        except ValueError:
            return False
        position.append(currentPosition)
    return position
