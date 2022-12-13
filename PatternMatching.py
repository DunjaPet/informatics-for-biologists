def PatternMatching(Pattern, Genome):
    positions = [] 
    #count = 0 # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            #count = count+1
            positions.append(i)
    return positions
