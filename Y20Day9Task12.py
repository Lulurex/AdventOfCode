import numpy as np

# Set up read file
#with open('inputDec9test.txt', 'r') as file:
#    raw = [int(number) for number in file.readline()]


f = open("inputDec9.txt", "r")
soraw = f.read().splitlines()   # list of strings
raw = [int(y) for y in soraw]   # list of ints

#list = array(raw)
#my_array = [y for y in list]
#my_array = np.asarray(my_array) #create a numpy array

                           # running set of values searched for sum
prelength = 25
preamble = []

def twoSum(sum, window):        # want to have find a sum. return (and the sum) when no sum found, ret true when sum found

    sumPool = set()  # later version would not have to reset sumpool

    k=len(window)-1
    for w in range(len(window)):  # for index 0 to window length - 1, iterate over 1,2,..window
        sub = sum - window[w]       # find the subtraction of sub = sum - window[i]

        if sub in sumPool:                      # if sub is in the pool, then we're done.
#            print(str(sum) + " = " + str(window[w]) + " + " + str(sub))
            return False                         # Sum found
        else:                           # Otherwise Add it to the set of "not correct".
            sumPool.add(window[w])

    # Did not find a sum ever
#    print("window is: ")
#    print(window)
#    print("sum is " + str(sum))
    return sum                                  # NO sum found, this is the answer.



for i in range(prelength): # Add first numbers to the set
    preamble.append(raw[i])

i = 0
j = len(raw)-1
for i in range(prelength,len(raw)-1): # Find the sums
    a = twoSum(raw[i], preamble)
#    print("iteration: " + str(i))
    if a != False:
        break
    preamble.remove(raw[i-prelength])
    preamble.append(raw[i])

print("sum is: " + str(a))
roller = []
# Part 2 contiguous sum, min and max
for r in range(i):
#    print(roller)
    roller.append(raw[r])
    rollingsum = sum(roller)
    while rollingsum > a:
        roller.remove(roller[0])
        rollingsum = sum(roller)
        if rollingsum == a:       # Found the correct window
            print("found windowed sum:")
            print(roller)
            break
    if rollingsum == a:  # Found the correct window
        break

# Print the answer of the min + max
print("answer is: " + str(min(roller)+max(roller)))

f.close()
