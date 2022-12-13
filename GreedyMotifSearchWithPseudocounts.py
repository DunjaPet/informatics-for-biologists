# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = [] # output variable
    for i in range(0,t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    BestMotifsScore = Score(BestMotifs)
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < BestMotifsScore:
            BestMotifs = Motifs
            BestMotifsScore = Score(BestMotifs)
    return BestMotifs

# Copy all needed subroutines here.  These subroutines are the same used by GreedyMotifSearch(),
# except that you should replace Count(Motifs) and Profile(Motifs) with the new functions
# CountWithPseudocounts(Motifs) and ProfileWithPseudocounts(Motifs).
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])  
    profile = {} # output variable
    pseudocount=CountWithPseudocounts(Motifs)
    for symbol in "ACGT":
        profile[symbol] = []
        for j in range(k):
             profile[symbol].append(0)
    for j in range(k):
        for symbol in 'ACGT':
            profile[symbol][j]=pseudocount[symbol][j]/(t+4)
    return profile

def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {} # output variable
    for symbol in "ACGT":
        count[symbol] = []  #4 emty rows for each symbol (ACGT)
        for j in range(k):
             count[symbol].append(1)   #4 rows filled with 1s instead of 0s
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Consensus(Motifs):
    # insert your code here
    consensus = ""
    count=ProfileWithPseudocounts(Motifs)  #count works with both Profile and Count
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

# Then copy your ProfileMostProbablePattern(Text, k, Profile) and Pr(Text, Profile) functions here.
def Pr(Text, Profile):
    Pr=1
    for i in range(len(Text)):
        Pr*=Profile[Text[i]][i]
    return Pr

def ProfileMostProbablePattern(Text, k, Profile):
    max_probability = -1
    for i in range(len(Text)-k+1):
        current_probability = 1
        substring = Text[i:i+k]
        for j, nucleotide in enumerate(substring):
            current_probability=Pr(substring,Profile)
            
        if current_probability > max_probability:
            max_probability = current_probability
            Pattern = substring
    return Pattern
