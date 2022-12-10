'''
shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
'''

path = 'input.txt'

with open(path, 'r') as f:
    data = f.readlines()

data = [(value.strip()) for value in data]
print(data)

values = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
output = 0
# Check if the data length is dividable by 3

if len(data)%3 == 0:
    for line in data:
        first_half  = set(line[0:int(len(line)/2)])
        second_half = set(line[int(len(line)/2):len(line)])
        diff = list(second_half.intersection(first_half))

        # output += values.index(diff[0])+1

    # print(output)
else:
    print('wrong data length!')
# Second half
def calculate_intersection(input, group_size):
    t = set(input[0])
    for ii in range(group_size-1):
        t = t&set(input[ii+1])
    return list(t)

group_size = 2

if len(data)%group_size == 0:

    for ii in range(int(len(data)/3)):
        group = (data[ii*group_size:group_size*(ii+1)])
        intersection_value = calculate_intersection(group, group_size)
        output += values.index(intersection_value[0]) + 1
else:
    print('wrong data length!')

print(output)
