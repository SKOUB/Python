def distance_hamming(m1,m2):
    d = 0
    for a,b in zip(m1,m2):
        if a != b :
            d = d + 1
    return d

print(distance_hamming("boire", "boite"))