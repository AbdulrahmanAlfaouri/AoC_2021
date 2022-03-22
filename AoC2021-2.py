import re

with open("input.txt") as measures:
    text = measures.read()



regex = re.compile("d\s\d|n\s\d|p\s\d")
forwardregex = re.compile("d\s\d")
downregex = re.compile("n\s\d")
upregex = re.compile("p\s\d")

cords = regex.findall(text)
cords_value = [int(value[-1]) for value in cords]
print(cords)
print(cords_value)

for act_value in cords:
    print(act_value)

forward = forwardregex.findall(text)
down = downregex.findall(text)
up = upregex.findall(text)


downvalue = [int(value[-1]) for value in down]
upvalue = [int(value2[-1]) for value2 in up]
forwardvalue = [int(value3[-1]) for value3 in forward]

aim = sum(downvalue) - sum(upvalue)
print(sum(forwardvalue), sum(downvalue) , sum(upvalue))

print(forwardvalue)
print(downvalue)
print(upvalue)

