moutarde = "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"
rose = "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"
pervenche = "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC"
leblanc = "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"


def adn1(sequence):

    if sequence.count('CATA') != 0:
        return 0
    else :
        return 1


def adn2(sequence):
    if sequence.count('ATGC') != 0:
        return 0
    else:
        return 1


list_suspect = [moutarde, rose, pervenche, leblanc]

for i in list_suspect:
    if (adn1(i) != 0 and adn2(i) != 0) and (adn2(i) > adn1(i)+4 or adn2(i) < adn1(i)+1):
        if i == "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC":
            print("Moutarde est coupable")
        elif i == "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG":
            print("Rose est coupable")
        elif i == "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC":
            print("Pervenche est coupable")
        elif i == "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG":
            print("Leblanc est coupable")
