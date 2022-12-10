path = 'input.txt'

with open(path, 'r') as f:
    data = f.read()

window_size = 14
print(len(data)-window_size)

t = {}
ii = 0
while (len(t) != window_size):
    t = set(data[ii:ii+window_size])

    # print(ii)
    ii += 1

print(ii+window_size-1)