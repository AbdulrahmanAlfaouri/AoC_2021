with open("input.txt") as measures:
    text = measures.readlines()

fulltext = [line.strip('\n') for line in text]
bites = []
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

    gamma = '0' if zero_count > one_count else '1'
    epsilon = '1' if zero_count > one_count else '0'

    gamma_bites.append(gamma)
    epsilon_bites.append(epsilon)

binarry_gamma = ''.join(gamma_bites)
binarry_epsilon = ''.join(epsilon_bites)

print(binarry_gamma)
print(binarry_epsilon)
