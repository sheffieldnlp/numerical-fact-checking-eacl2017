from collections import defaultdict


def bow(a,b):
    counts_a = defaultdict(lambda:0)
    counts_b = defaultdict(lambda:0)

    for word in a:
        counts_a[word] +=1

    for word in b:
        counts_b[word] +=1


    vec_a = []
    vec_b = []

    for key in set(counts_a.keys()).union(counts_b.keys()) :
        vec_a.append(counts_a[key])
        vec_b.append(counts_b[key])

    return vec_a,vec_b


def character_ngram(word,n=3):
    if(len(word)<n):
        return word
    return [word[i:i+n] for i in range(len(word)-n+1)]

