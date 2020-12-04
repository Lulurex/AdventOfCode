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


hitTrees = [0]

dx = 3  # change in x
dy = 1  # change in y

lineLength = len(my_array[1])
x = 0   # x position
y = 0   # y position

for i in range(len(my_array)-1):
    x += dx  # move to next location
    y += dy

    if x >= lineLength:  # check out of bounds
        x = convert(x, lineLength)
    print("iteration: " + str(i))
    print(my_array[y][x])
    if '#' == my_array[y][x]:
        print("hit")
        hitTrees += 1

print(hitTrees)

#my array y x
#aline = my_array[1][0]
#print(aline)
#print(my_array[1])
    #Check Tree status



    #print("iteration:" + str(i))
    #print(x)
    #print(y)






f.close()
