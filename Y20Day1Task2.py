import numpy as np
#Day 1 Task 2. Do the same but for 3 numbers that sum to 2020, and multiply to get the answer.
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
answer = 0;
for roundone in range(199):
    for roundtwo in range(199):
        first = my_array[roundone]
        second = my_array[roundtwo]

        sub = 2020 - my_array[roundone] - my_array[roundtwo]



        print("first value: " + str(first))
        print("second value: "+ str(second))
        print("looking for: "+ str(sub))

        x = np.where(my_array == sub)# search for the opposite, x is the tuple
        print(x[0])

        if len(x[0]) == 1:
            print("Found\n")
            answer = first*second*sub  #original * subtracted value
            print("Answer: ")
            print(answer)
            break

        else:
            print("Still looking\n")
            if roundone==199 & roundtwo == 199:
                print("nothing")
    if answer > 0:
        break

f.close()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
