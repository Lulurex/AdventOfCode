import numpy as np

f = open("inputDec10.txt", "r")
soraw = f.read().splitlines()   # list of strings
raw = [int(y) for y in soraw]   # list of ints

# Sort the list
max = max(raw)
index = []

for i in range(max):    # Create an array of 0's up to max number
    index.append(0)

for j in range(len(raw)):   # Input the numbers
    index[raw[j]-1] = raw[j]

while 0 in index:   # Remove the 0's
    index.remove(0)

index.insert(0,0)   # Account for 0 volt start.
print(index)

# find the Differences
ones = 0
threes = 1
for k in range(len(index)-1):       # Go through adjacent numbers, and count differences
    dif = index[k+1] - index[k]

    if dif == 1:
        ones += 1

    if dif == 3:
        threes += 1

print(ones)
print(threes)
print("mult = " + str(ones*threes))

f.close()
