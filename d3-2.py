with open("input.txt") as measures:
    text = measures.readlines()
aaa = []

fulltext = [line.strip('\n') for line in text]
for l in range(12):

    biites = [i[l] for i in  fulltext]
    ones = biites.count('1')
    zeros = biites.count('0')
    a = '1' if ones >= zeros else '0'
    for j in fulltext:
        if j[l] != a:
            aaa.append(j)
    for k in aaa:
        fulltext.remove(k)
    aaa.clear()

print(fulltext)

fulltext = [line.strip('\n') for line in text]

for l in range(12):
    if len(fulltext) == 1:
        print(fulltext)

    biites = [i[l] for i in  fulltext]
    ones = biites.count('1')
    zeros = biites.count('0')
    a = '0' if zeros <= ones else '1'
    for j in fulltext:
        if j[l] != a:
            aaa.append(j)
    for k in aaa:
        fulltext.remove(k)
    aaa.clear()







