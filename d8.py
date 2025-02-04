with open("input.txt") as in_text:
    in_digits = in_text.readlines()

outsum = 0

for line in in_digits:
    output_digits = line.split("|")[1].split()
    unique_signal_patterns = line.split("|")[0].split()

    all_numbers = {
        "zero": '',
        "one": '',
        "tow": '',
        "three": '',
        "four": '',
        "five": '',
        "six": '',
        "seven":'',
        "eight":  '',
        "nine":'',
    }


    up = ""
    down = ""
    middle = ""
    upright = ""
    upleft = ""
    downright = ""
    downleft = ""

    output = []
    towAndthreeAndfive = []
    nineAndzeroAndsix = []
    downAndDownleft = []
    fiveAndthree = []

    for digit in unique_signal_patterns:
        if len(digit) == 3:
            all_numbers["seven"] = digit  # 7
        elif len(digit) == 7:
            all_numbers["eight"] = digit  # 8
        elif len(digit) == 4:
            all_numbers["four"] = digit  # 4
        elif len(digit) == 2:
            all_numbers["one"] = digit  # Got one
        elif len(digit) == 6:  # 9 or 6 or 0
            nineAndzeroAndsix.append(digit)
        elif len(digit) == 5:  # 5 or 2 or 3
            towAndthreeAndfive.append(digit)

    for digit1 in unique_signal_patterns:
        for segment in digit1:
            if (segment in all_numbers['seven']) and (segment not in all_numbers['one']):
                up = segment  # up segment
            elif (
                (segment in all_numbers['eight'])
                and (segment not in all_numbers['four'])
                and (segment != up)
                and (downAndDownleft.count(segment) < 1)
            ):
                downAndDownleft.append(segment)



    for segment2 in downAndDownleft:
        for digit2 in towAndthreeAndfive:
            if segment2 not in digit2:
                fiveAndthree.append(digit2)
                downleft = segment2  # down L segment

    all_numbers['tow'] = "".join([i for i in towAndthreeAndfive if i not in fiveAndthree])  # 2
    downAndDownleft.remove(downleft)
    down = downAndDownleft[0]  # down segment

    for digit3 in fiveAndthree:
        for segment in digit3:
            if segment not in all_numbers["tow"]:
                downright = segment

    nine = "".join([i for i in all_numbers["eight"] if i != downleft])  # 9
    nineOrd = sum([ord(i) for i in all_numbers["nine"]])
    for digit4 in nineAndzeroAndsix:
        digit4Ord = sum([ord(j) for j in digit4])
        if digit4Ord == nineOrd:
            nine = digit4

    nineAndzeroAndsix.remove(all_numbers["nine"])
    sixAndZero = nineAndzeroAndsix

    upleftAndDownright = [i for i in all_numbers["eight"] if i not in all_numbers["tow"]]

    for segment3 in upleftAndDownright:
        for digit6 in fiveAndthree:
            if segment3 not in digit6:
                all_numbers["three"] = digit6  # 3
                break

    fiveAndthree.remove(all_numbers["three"])
    five = fiveAndthree[0]  # 5

    for digit6 in sixAndZero:
        for onesegment in all_numbers["one"]:
            if onesegment not in digit6:
                all_numbers["six"] = digit6  # 6
                break

    sixAndZero.remove(all_numbers["six"])
    all_numbers["zero"] = sixAndZero[0]


    for key in all_numbers:
        numlist = [i for i in all_numbers[key]]
        numlist.sort()
        all_numbers[key] = "".join(numlist)

    for outdigit in output_digits:
        outdigitlist = [i for i in outdigit]
        outdigitlist.sort()
        outdigit = "".join(outdigitlist)

        if outdigit == all_numbers["zero"]:
            output.append("0")
        elif outdigit == all_numbers["one"]:
            output.append("1")
        elif outdigit == all_numbers["tow"]:
            output.append("2")
        elif outdigit == all_numbers["three"]:
            output.append("3")
        elif outdigit == all_numbers["four"]:
            output.append("4")
        elif outdigit == all_numbers["five"]:
            output.append("5")
        elif outdigit == all_numbers["six"]:
            output.append("6")
        elif outdigit == all_numbers["seven"]:
            output.append("7")
        elif outdigit == all_numbers["eight"]:
            output.append("8")
        elif outdigit == all_numbers["nine"]:
            output.append("9")
        else:
            output.append(f"shit what the fuck is {outdigit}")

    print(output)
    outsum += int("".join(output))

print(outsum)