import hashlib

def hamming_distance(chaine1, chaine2):
    return sum(c1 != c2 for c1, c2 in zip(chaine1, chaine2))

def hamming_distance2(chaine1, chaine2):
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(chaine1, chaine2))))

if __name__=="__main__":    
    chaine1 = hashlib.md5("chaine1".encode()).hexdigest()
    chaine2 = hashlib.md5("chaine2".encode()).hexdigest()

    #chaine1 = "6fb17381822a6ca9b02153d031d5d3da"
    #chaine2 = "a242eace2c57f7a16e8e872ed2f2287d"

    assert len(chaine1) == len(chaine2)

    print(hamming_distance(chaine1, chaine2))

    print(hamming_distance2(chaine1, chaine2))

# prim = "ffd3c181818181ff"
# seg = "e3c38787878d8f81"
# print(len(prim))
# print(len(seg))

# print(''.join(format(ord(i), 'b') for i in prim))
# print(len(''.join(format(ord(i), 'b') for i in prim)))

# has = "1111111111010011110000011000000110000001100000011000000111111111"
# has2 = "1110001111000011100001111000011110000111100011011000111110000001"


# print(len(has))
# print(len(has2))

# diff = 0

# for i in range(0,len(has),1):
#     if has[i] == has2[i]:
#         pass
#     else:
#         diff = diff +1

# print(has)
# print(has2)
# print(diff)

# print(diff/64*100)

# hamming_distance = hamming(has, has2)
# print(hamming_distance)


