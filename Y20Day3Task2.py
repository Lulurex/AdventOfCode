import numpy as np

# Set up read file
f = open("inputDec3.txt", "r")
raw = f.read().splitlines()
list = np.asarray(raw)
my_array = [y for y in list]   #change to ints array
my_array = np.asarray(my_array) #create a numpy array
#print(my_array)

def convert(a, length):
    while a >= length:
        a = a - length
    return a


hitTrees = [0, 0, 0, 0, 0]

dx = [1, 3, 5, 7, 1]  # change in x
dy = [1, 1, 1, 1, 2]  # change in y

lineLength = len(my_array[1])
x = 0  # x position
y = 0  # y position

for slope in range(5):
    x = 0  # x position
    y = 0  # y position

    for i in range(len(my_array)-1):
        x += dx[slope]  # move to next location
        y += dy[slope]

        if x >= lineLength:  # check out of bounds
            x = convert(x, lineLength)

        if y >= len(my_array):
            break
        #print("iteration: " + str(i))
        #print(my_array[y][x])

        if '#' == my_array[y][x]:
            hitTrees[slope] += 1

    print(hitTrees)

product = 1
for p in range(len(hitTrees)):
    product = product * hitTrees[p]
print(product)

f.close()
