import numpy as np

# Set up read file
f = open("inputDec5.txt", "r")
raw = f.read().splitlines()
list = np.array(raw)
my_array = [y for y in list]
my_array = np.asarray(my_array) #create a numpy array

greatestNumber = 0
lowestNumber = 1000000

def binToDec(b):
    decNum = int(b, 2)
    return decNum

numbers = []

for i in range(len(my_array)):
    newN = 0
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

#    print((binToDec(row) * 8) + binToDec(col))
    newN = (binToDec(row) * 8) + binToDec(col)

    numbers.append(newN)

    if greatestNumber < newN:
        greatestNumber = newN
    if newN < lowestNumber:
        lowestNumber = newN

print("end:" + str(greatestNumber))
print("end: " + str(lowestNumber))
#print(numbers)

for x in range(lowestNumber, greatestNumber):
    if x not in numbers:
        print("missing" + str(x))

f.close()
