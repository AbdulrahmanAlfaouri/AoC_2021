with open("input.txt") as full_text:
    text = full_text.readlines()

def extract_binary_numbers():
    unwanted_numbers = []
    binary_numbers = []
    for rating in ["CO2", "oxygen"]:
        measures = [line.strip("\n") for line in text]
        for num in range(12):
            bites = [bitsNum[num] for bitsNum in measures]

            ones = bites.count("1")
            zeros = bites.count("0")

            if rating == "CO2":
                bite = "1" if ones >= zeros else "0"
            else:
                bite = "0" if zeros <= ones else "1"

            for decimal_num in measures:
                if decimal_num[num] != bite:
                    unwanted_numbers.append(decimal_num)

            for unwated_number in unwanted_numbers:
                measures.remove(unwated_number)

            unwanted_numbers.clear()

            if len(measures) == 1:
                binary_numbers.append(measures[0])

    return binary_numbers


def get_final_score(binary_numbers):
    final_score_numbers = []
    for bi_number in binary_numbers:
        dec_number = int(bi_number, 2)
        final_score_numbers.append(dec_number)
    return final_score_numbers[0] * final_score_numbers[1]


bi_numbers = extract_binary_numbers()
final_score = get_final_score(bi_numbers)

print(final_score)
