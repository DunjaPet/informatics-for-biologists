# import the random package here
import random
# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 

# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.
def RandomMotifs(Dna, k, t):
    t =len(Dna)
    M =len(Dna[0])  #M=len(Dna[0]) is a lenght of the first row 
    RandomMotifs=[]
    for i in range(t):
        rand=random.randint(1,M-k)                     
        RandomMotifs.append(Dna[i][rand:rand+k])
    return RandomMotifs

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

def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
    max_probability = -1
    for i in range(len(Text)-k+1):
        current_probability = 1
        for j, nucleotide in enumerate(Text[i:i+k]):
            current_probability=Pr(Text[i:i+k],Profile)
            
        if current_probability > max_probability:
            max_probability = current_probability
            Pattern = Text[i:i+k]
    return Pattern

def Motifs(Profile, Dna):
    Motifs=[]
    t=len(Dna)
    #k=4
    for i in range(t):
        Motifs.append(ProfileMostProbablePattern(Dna[i], k, Profile))
    return Motifs

def Pr(Text, Profile):   #probability
    Pr=1
    for i in range(len(Text)):
        Pr*=Profile[Text[i]][i]
    return Pr

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

def Score(Motifs):
    score=0
    consensus=Consensus(Motifs)
    for m in Motifs:
        score+= HammingDistance(m, consensus)
    return score

def HammingDistance(p, q):
    diff=0
    for i in range(len(q)):
        if p[i]!=q[i]:
            diff+=1
    return diff

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
def RepeatedRandomizedMotifSearch(Dna, k, t):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(1000):
        Motifs = RandomizedMotifSearch(Dna, k, t)
        CurrScore = Score(Motifs)
        if CurrScore < BestScore:
            BestScore = CurrScore
            BestMotifs = Motifs
    return BestMotifs
