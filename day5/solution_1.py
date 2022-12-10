def readlines_ext(file, line_numbers):
    with open(file, 'r') as fp:
        # To store lines
        lines = []
        for i, line in enumerate(fp):
            # read line 4 and 7
            if i in line_numbers:
                lines.append(line.strip())
            elif i > line_numbers[-1]:
                # don't read after line 7 to save time
                break
    return lines

path = 'input.txt'

with open(path, 'r') as f:
    data_raw = f.readlines()
data = [value.strip() for value in data_raw]

input_size = int(data[data.index('') - 1].split()[-1])

with open(path, 'r') as f:
    data_head = [next(f).strip('\n') for ii in range(data.index('') - 1)]

line_numbers = range(data.index('') + 1, len(data))
data_rules = readlines_ext(path, line_numbers)
data_rules = [rule.split(' ')[1::2] for rule in data_rules]

column = []
for jj in range(input_size):
    l = []
    for ii in range(len(data_head)):
        t = data_head[ii][jj * 4:jj * 4 + 3]
        if t != '   ':
            l.append(t.strip('[').strip(']'))
    column.append(l)

print(column)
print(data_rules)

# for rule in data_rules:
#     # save, remove, append
#     print(rule)
#     t = column[int(rule[1]) - 1][0:int(rule[0])]  # saved moving crates
#     del column[int(rule[1]) - 1][0:int(rule[0])]  # remove items
#     for crate in t:
#         column[int(rule[2]) - 1].insert(0, crate) # insert a new one
#
# top = [v[0] for v in column]
# output = ''
# for i in top:
#     output += i
# print(output)

# Part 2
for rule in data_rules:
    # save, remove, append
    print(rule)
    t = column[int(rule[1]) - 1][0:int(rule[0])]  # saved moving crates
    del column[int(rule[1]) - 1][0:int(rule[0])]  # remove items

    for crate in t[::-1]:
        column[int(rule[2]) - 1].insert(0, crate) # insert a new one

top = [v[0] for v in column]
output = ''
for i in top:
    output += i
print(output)
