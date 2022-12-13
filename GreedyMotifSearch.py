# Copy your Score(Motifs), Count(Motifs), Profile(Motifs), and Consensus(Motifs) functions here.
def Profile(Motifs):
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
            
    
    for j in range(k):
        for symbol in 'ACGT':
            count[symbol][j]=count[symbol][j]/t 
          
    return count
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

# Then copy your ProfileMostProbablePattern(Text, k, Profile) and Pr(Text, Profile) functions here.
def Pr(Text, Profile):
    # insert your code here
    Pr=1
    for i in range(len(Text)):
        Pr*=Profile[Text[i]][i]
    return Pr
# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
    max_probability = -1
    for i in range(len(Text)-k+1):
        current_probability = 1
        for j, nucleotide in enumerate(Text[i:i+k]):
            current_probability=Pr(Text[i:i+k],Profile)
            
        if current_probability > max_probability:
            max_probability = current_probability
            Pattern = Text[i:i+k]
    return Pattern
# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    # type your GreedyMotifSearch code here.
    BestMotifs = []
    for i in range(0,t):
        BestMotifs.append(Dna[i][0:k])
        n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
        
