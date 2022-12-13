def Skew(Genome):
    skew = {} #initializing the dictionary
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
