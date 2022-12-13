# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = reverse(complement(Pattern))
    # your code here
    return revComp


# Copy your reverse function from the previous step here.
def reverse(Pattern):
    seq=list(Pattern)
    rev_string=seq[::-1]
    seq = ''.join(rev_string)
    return seq

# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Pattern):
    comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    bases = list(Pattern) 
    bases = [comp[base] for base in bases]
    bases = ''.join(bases)
    return bases
