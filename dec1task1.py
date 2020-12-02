import numpy as np

# Set up read file
f = open("adventDec1_1.txt", "r")
raw = f.read().splitlines()
list = np.asarray(raw)
my_array = [int(y) for y in list]   #change to ints array
my_array = np.asarray(my_array) #create a numpy array

""" Debug Exploration
print(my_array)
arr = np.array([1721,979,366,299,675,1456])
print (arr)
t = np.where(arr == 201) #tuple
print(t)
print("This is it: ")
print(len(t[0]))
print("\n")
"""

for i in range(199):
    first = my_array[i]
    sub = 2020 - first

    print("first value: " + str(first))
    print("looking for: "+ str(sub))

    x = np.where(my_array == sub)# search for the opposite, x is the tuple
    print(x[0])

    if len(x[0]) == 1:
        print("Found\n")
        answer = first*sub  #original * subtracted value
        print("Answer: ")
        print(answer)
        break
    else:
        print("Still looking\n")
        if i==199:
            print("nothing")

f.close()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
