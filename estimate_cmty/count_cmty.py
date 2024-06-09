import os
from collections import Counter

#read file
input_path = './estimate_value/'
file = os.listdir(input_path)
with open(input_path + 'all_dataset.dat', 'w') as file1:
    for f in file:
        if f.endswith('.dat'):
            continue
        time = ''

        with open(input_path + f, 'r') as file2:
            lines = file2.readlines()
            count = list()
            for line in lines[1:-1]:
                iter,value,_,_ = line.split()
                count.append(value)
            time = lines[-1]
        # print(f, Counter(count).most_common)
        # file1.write(f + '\t' + str(Counter(count).most_common()) + '\n')
        file1.write(f.split('.')[0] + '\t' + str(Counter(count).most_common(1)[0][0]) + '\n')
        file1.write(time)


