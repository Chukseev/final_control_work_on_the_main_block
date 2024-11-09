array = ['Hello', '2', 'world', ':-)']
res_array = []

for i in range(len(array)):
    if len(array[i]) <= 3:
        res_array.append(array[i])
    i += 1

print(res_array)