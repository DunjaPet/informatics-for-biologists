def Normalize(Probabilities):
    sumvalue=sum(Probabilities.values())
    for key, value in enumerate(Probabilities):
        Probabilities[value]=Probabilities[value]/sumvalue
    return Probabilities
