def WeightedDie(Probabilities):
    kmer = ''
    kmers=list(Probabilities.keys())
    p=random.uniform(0, 1)
    n = 0
    for key, value in Probabilities.items():
        n += value
        if p < n:
            return key
        continue
        start=0
        end=Probabilities[value]
        count=0
        if start<p<end:
            kmer=kmers[count]
        start+=Probabilities[value]
        end+=Probabilities[value]
        count+=count
    assert 0
    return kmer
