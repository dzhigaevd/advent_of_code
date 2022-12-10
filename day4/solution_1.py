def check_containment(pair):
    if int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]):
        return 1
    elif int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1]):
        return 1
    else:
        return 0


def check_overlap(pair):
    if int(pair[0][1]) >= int(pair[1][0]) and int(pair[0][0]) <= int(pair[1][1]):
        return 1
    else:
        return 0


path = 'input.txt'

with open(path, 'r') as f:
    data = f.readlines()

data = [value.strip() for value in data]
pairs = [(pair.split(',')) for pair in data]
ranges = []
for pair in pairs:
    ranges.append([v.split('-') for v in pair])
print(ranges)
count = 0

for pair in ranges:
    count += check_containment(pair)

print(count)
# Second part

count = 0

for pair in ranges:
    count += check_overlap(pair)

print(count)