# first, import the random package
import random

# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def GibbsSampler(Dna, k, t, N):
    BestMotifs = [] 
    Motifs = RandomMotifs(Dna, k, t)   #random motifs selected in each DNA string 
    BestMotifs = Motifs
    for j in range(N):
        i=random.randint(0,t-1)
        #if i not in M.index():
        Profile=ProfileWithPseudocounts(Motifs[:i] + Motifs[i+1:])   #ignoring M[i]
        Motif_i=ProfileGeneratedString(Motifs[i], Profile, k)
        if Score(Motifs) < Score(BestMotifs):
                BestMotifs = Motifs
        return BestMotifs

# place all subroutines needed for GibbsSampler below this line
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

def WeightedDie(Probabilities):
    kmer = ''
    kmers=list(Probabilities.keys())
    p=random.uniform(0, 1)
    n = 0
    for key, value in Probabilities.items():
        n += value
        if p < n:
            return key
        
def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {} 
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

def Pr(Text, Profile):   #probability
    Pr=1
    for i in range(len(Text)):
        Pr*=Profile[Text[i]][i]
    return Pr

def Profile(Motifs):
    count = {} # initializing the count dictionary
    k = len(Motifs[0])   #len creates one integer not a list therefore cannot be iterable!
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):  #range creates a iterable list out of integer
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
            
    
    for j in range(k):
        for symbol in 'ACGT':
            count[symbol][j]=count[symbol][j]/t 
          
    return count

def Normalize(Probabilities):
    sumvalue=sum(Probabilities.values())
    for key, value in enumerate(Probabilities):
        Probabilities[value]=Probabilities[value]/sumvalue
    return Probabilities

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

def Motifs(Profile, Dna):
    Motifs=[]
    t=len(Dna)
    for i in range(t):
        Motifs.append(ProfileMostProbablePattern(Dna[i], k, Profile))
    return Motifs

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

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
def RepeatedGibbsSampler(Dna, k, t, N):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(100):
        Motifs = GibbsSampler(Dna, k, t, N)
        CurrScore = Score(Motifs)
        if CurrScore < BestScore:
            BestScore = CurrScore
            BestMotifs = Motifs
    return BestMotifs
