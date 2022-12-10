path = 'input.txt'

with open(path, 'r') as f:
    data = f.readlines()

data = [(value.strip()) for value in data]

sum_value = 0
elv_value = []
for ii in range(len(data)):
    if data[ii] != '':
        sum_value += int(data[ii])
        if ii == (len(data)-1):
            elv_value.append(sum_value)
    else:
        elv_value.append(sum_value)
        sum_value = 0
        pass

elv_value.sort(reverse=True)
print(sum(elv_value[0:3]))
output = []
