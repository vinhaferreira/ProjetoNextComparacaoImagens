
prim = "ffd3c181818181ff"
seg = "e3c38787878d8f81"
print(len(prim))
print(len(seg))

has = "1111111111010011110000011000000110000001100000011000000111111111"
has2 = "1110001111000011100001111000011110000111100011011000111110000001"
print(len(has))
print(len(has2))

diff = 0

for i in range(0,len(has),1):
    if has[i] == has2[i]:
        pass
    else:
        diff = diff +1

print(has)
print(has2)
print(diff)

print(diff/64*100)

