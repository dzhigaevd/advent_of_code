'''
shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
'''

path = 'input.txt'

with open(path, 'r') as f:
    data = f.readlines()

data = [(value.strip()) for value in data]
print(data)
score = 0
win_pairs = ['A Y', 'B Z', 'C X']
loose_pairs = ['A z', 'B X', 'C Y']
draw_pairs = ['A X', 'B Y', 'C Z']

def choose_piese(pair):
    value = 0

    if pair[-1] == 'X':
        if pair[0] == 'A':
            value += 3
        elif pair[0] == 'B':
            value += 1
        elif pair[0] == 'C':
            value += 2

    if pair[-1] == 'Y':
        if pair[0] == 'A':
            value += 1
        elif pair[0] == 'B':
            value += 2
        elif pair[0] == 'C':
            value += 3

    if pair[-1] == 'Z':
        if pair[0] == 'A':
            value += 2
        elif pair[0] == 'B':
            value += 3
        elif pair[0] == 'C':
            value += 1

    return value

for pair in data:
    if pair[-1] == 'X':
        score += 0
    elif pair[-1] == 'Y':
        score += 3
    elif pair[-1] == 'Z':
        score += 6

    outcome = choose_piese(pair)
    score += outcome

print(score)

output = []
