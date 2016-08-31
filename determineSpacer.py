
def determineSpacer(seed, illegalSites):
    spacer = ""
    for eachBase in seed:
        if eachBase == 'A':
            spacer = spacer + 'G'
        elif eachBase == 'T':
            spacer = spacer + 'C'
        elif eachBase == 'G':
            spacer = spacer + 'T'
        elif eachBase == 'C':
            spacer = spacer + 'A'
    subs = map(list, zip(*(spacer[i:] for i in range(6)))) # all length 6 substrings of spacer
    for eachSubSeq in subs:
        for eachSite in illegalSites:
            if eachSubSeq == eachSite:
                return "fail " + eachSite + " found"
    return spacer

