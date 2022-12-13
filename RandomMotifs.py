# import Python's 'random' module here
import random
# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t):
    t =len(Dna)
    M =len(Dna[0])  #M=len(Dna[0]) is a lenght of the first row 
    RandomMotifs=[]
    for i in range(t):
        rand=random.randint(1,M-k)                     
        RandomMotifs.append(Dna[i][rand:rand+k])
    return RandomMotifs
