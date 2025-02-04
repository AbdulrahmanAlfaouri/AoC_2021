import re

with open("input.txt") as measures:
    text = measures.read()

regex = re.compile(r"d\s\d|n\s\d|p\s\d")
forward_regex = re.compile(r"d\s\d")
down_regex = re.compile(r"n\s\d")
up_regex = re.compile(r"p\s\d")

cords = regex.findall(text)
cords_value = [int(value[-1]) for value in cords]

forward = forward_regex.findall(text)
down = down_regex.findall(text)
up = up_regex.findall(text)

down_value = [int(value[-1]) for value in down]
up_value = [int(value2[-1]) for value2 in up]
forward_value = [int(value3[-1]) for value3 in forward]

aim = sum(down_value) - sum(up_value)
print(sum(forward_value), sum(down_value), sum(up_value))
