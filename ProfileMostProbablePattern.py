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
