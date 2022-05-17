import logging
from logging import info

logging.basicConfig(filename='test.txt', level=logging.INFO,format='%(message)s')
with open('input.txt') as text:
    in_text = [i.strip() for i in text.readlines()]

bracets1 = {'<':'>', '(':')', '{':'}', '[':']'}
bracets2 = {'>':'<', ')':'(', '}':'{', ']':'['}

def get_score_and_incomplete_lines(in_text):
    openings = []
    syntex_error_socre = 0
    not_corrupted = []

    for chunk in in_text:
        for char in chunk:
            if char in bracets1.keys():
                opening = char
                openings.append(opening)
            else:
                ending = char
                last_opening = openings[-1]
                if bracets1[last_opening] == ending:
                    openings.pop()
                    if chunk not in not_corrupted:
                        not_corrupted.append(chunk)
                else:
                    if ending == '}':
                        syntex_error_socre += 1197
                    if ending == ')':
                        syntex_error_socre += 3
                    if ending == '>':
                        syntex_error_socre += 25137
                    if ending == ']':
                        syntex_error_socre += 57
                    if chunk in not_corrupted:
                        not_corrupted.remove(chunk)
                    break

    return [syntex_error_socre, not_corrupted]

def get_added_openings(line):
    bracets2 = {'>':'<', ')':'(', '}':'{', ']':'['}
    list_line = list(line)
    list_line.reverse()
    reversed_line = ''.join(list_line)
    closings = []
    added_openings = []

    for character in reversed_line:
        if character in bracets2.keys():
            closings.append(character)
        else:
            if len(closings) != 0:
                lastest_closing = closings[-1]
                if character == bracets2[lastest_closing]:
                    closings.pop()
            else:
                added_openings.append(bracets1[character])

    return added_openings

def get_all_added_openings(incomplete_lines):
    all_added_openings = []
    for line in incomplete_lines:
        added = get_added_openings(line)
        all_added_openings.append(added)
    return all_added_openings

def get_total_scores(all_added_openeings):
    total_scores = []
    for added_closings in all_added_openeings:
        total_score = 0
        for char in added_closings:
            if char == '>':
                total_score *= 5
                total_score += 4
            if char == '}':
                total_score *= 5
                total_score += 3
            if char == ']':
                total_score *= 5
                total_score += 2
            if char == ')':
                total_score *= 5
                total_score += 1
        total_scores.append(total_score)

    return total_scores


errors_score, incomplete_lines = get_score_and_incomplete_lines(in_text)
added_closings = get_all_added_openings(incomplete_lines)
added_closings = [''.join(i) for i in added_closings]
total_scores = get_total_scores(added_closings)
total_scores.sort()
middle = int(len(total_scores)/2)


info(total_scores[middle])