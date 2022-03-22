import re

with open("input.txt") as measures:
    text = measures.read()

regex = re.compile("d\s\d|n\s\d|p\s\d")
forwardregex = re.compile("d\s\d")
downregex = re.compile("n\s\d")
upregex = re.compile("p\s\d")

cords = regex.findall(text)
depth = 0
aim = 0
hzposition = 0

for i in cords:
    forward = forwardregex.search(i)
    up = upregex.search(i)
    down = downregex.search(i)
    if forward is not None:
        hzposition += int(forward.group(0)[-1])
        depth += aim * int(forward.group(0)[-1])
        print(hzposition, f'depth={depth}', 'forward')
    if up is not None:
        aim -= int(up.group(0)[-1])
        print(aim,'up')
    if down is not None:
        aim += int(down.group(0)[-1])
        print(aim, 'down')

print(depth * hzposition)


