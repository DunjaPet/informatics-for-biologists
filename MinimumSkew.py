# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    t = Skew(Genome)
    mini = min(t.values())
    for i in t:
        if t[i] == mini:
            positions.append(i)
    return positions

# Input:  A String Genome
# Output: Skew(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def Skew(Genome):
    skew = {} # output variable
    n =len(Genome)
    skew[0]=0
    for i in range(1,n+1):
        if Genome[i-1]=="G":
            skew[i]= skew[i-1]+1
        elif Genome[i-1]=="C":
            skew[i]= skew[i-1]-1
        else:
            skew[i]=skew[i-1]
    return skew
