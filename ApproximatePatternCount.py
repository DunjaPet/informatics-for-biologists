# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    for i in range(len(Text)-len(Pattern)+1):
        mismatch=HammingDistance (Text[i:i+len(Pattern)],Pattern)
        if mismatch <= d:
            count+=1
    return count


# Insert your HammingDistance function on the following line.
def HammingDistance(p, q):
    mismatch=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            mismatch+=1
    return mismatch
