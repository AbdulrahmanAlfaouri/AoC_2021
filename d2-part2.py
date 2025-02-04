import re

with open("input.txt") as measures:
    text = measures.read()

regex = re.compile(r"d\s\d|n\s\d|p\s\d")
forward_regex = re.compile(r"d\s\d")
down_regex = re.compile(r"n\s\d")
up_regex = re.compile(r"p\s\d")
coords = regex.findall(text)

depth = 0
aim = 0
hzposition = 0

for coordinate in coords:
    forward = forward_regex.search(coordinate)
    up = up_regex.search(coordinate)
    down = down_regex.search(coordinate)

    if forward is not None:
        hzposition += int(forward.group(0)[-1])
        depth += aim * int(forward.group(0)[-1])
        print(hzposition, f"depth={depth}", "forward")

    if up is not None:
        aim -= int(up.group(0)[-1])
        print(aim, "up")

    if down is not None:
        aim += int(down.group(0)[-1])
        print(aim, "down")

print(depth * hzposition)
