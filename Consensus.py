# Copy your Consensus(Motifs) function here.
def Consensus(Motifs):
    # insert your code here
    consensus = ""
    count=Count(Motifs)
    k=len(Motifs[0])
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol  #this code adds up letters (ACGT)into one string(consensus)
    return consensus
# Copy your Count(Motifs) function here.

def Count(Motifs):
    count = {} # initializing the count dictionary
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.

def HammingDistance(p, q):
    diff=0
    for i in range(len(q)):
        if p[i]!=q[i]:
            diff+=1
    return diff


def Score(Motifs):
    score=0
    consensus=Consensus(Motifs)
    for m in Motifs:
        score+= HammingDistance(m, consensus)
    return score
