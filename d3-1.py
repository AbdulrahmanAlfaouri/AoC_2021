with open("input.txt") as measures:
    text = measures.readlines()

fulltext = [line.strip('\n') for line in text]
bites = []
# bites = [[],[],[],[],[]]
gamma_bites = []
epsilon_bites = []

for extend in fulltext:
    for nn in extend:
        bites.append([])
    break

for num in fulltext:
    for jj in range(len(num)):
        bites[jj].append(num[jj])



for j in bites:
    zero_count = j.count('0')
    one_count = j.count('1')
    if zero_count > one_count:
        gamma_bites.append('0')
        epsilon_bites.append('1')
    else:
        gamma_bites.append('1')
        epsilon_bites.append('0')

binarry_gamma = ''.join(gamma_bites)
binarry_epsilon = ''.join(epsilon_bites)

print(binarry_gamma)
print(binarry_epsilon)

# 1407
# 2688