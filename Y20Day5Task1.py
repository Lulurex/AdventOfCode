import numpy as np

# Set up read file
f = open("inputDec5.txt", "r")
raw = f.read().splitlines()
list = np.array(raw)
my_array = [y for y in list]
my_array = np.asarray(my_array) #create a numpy array

greatestNumber = 0
def binToDec(b):
    binaryNum = int(b, 2)
    return binaryNum

for i in range(len(my_array)):

#    print(my_array[0:7])
#    print(my_array[i][7:10])
    row = my_array[i][0:7]
    col = my_array[i][7:10]

    row = row.replace('B', '1')
    row = row.replace('F', '0')

    col = col.replace('R', '1')
    col = col.replace('L', '0')
#    print(row)
#    print(col)

    print((binToDec(row) * 8) + binToDec(col))
    newN = (binToDec(row) * 8) + binToDec(col)

    if greatestNumber < newN:
        greatestNumber = newN

print("end:" + str(greatestNumber))
#for i in range(0,len(my_array), 2):
#    print((binToDec(my_array[i]) * 8) + binToDec(my_array[i+1]))

f.close()
