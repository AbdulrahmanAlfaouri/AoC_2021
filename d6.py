fshees = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

with open('input.txt') as in_text:
    in_nums = in_text.readline().split(',')
    in_nums = [int(i) for i in in_nums]

for num in in_nums:
    for key in fshees:
        if num == key:
            fshees[key] += 1


fishs = {6:0, 8:0}


def shift():
    fishs[6] = fshees[0]
    fishs[8] = fshees[0]

    for key in fshees:
        try:
            fshees[key] = fshees[key + 1]
        except KeyError:
            pass


def addshit():
    fshees[8] = fishs[8]
    fshees[6] += fishs[6]


for day in range(256):
    shift()
    addshit()


theSum = list(fshees.values())
print(sum(theSum))

