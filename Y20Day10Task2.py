"""
Adapter Array
Advent of Code Day 10
https://adventofcode.com/2020/day/10
"""
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

index.insert(0,0)   # Account for 0 volt start
index.append(max+3)     # Account for +3 V rating
#print(index)

# find the Differences
ones = 0
twos = 0
threes = 0

differs = []  # differs is keeping track of the min differences between numbers

for k in range(len(index)-1):       # Go through adjacent numbers, and count differences
    dif = index[k+1] - index[k]

    if dif == 1:
        ones += 1
        differs.append(1)
    elif dif == 2:      # Note here that there are actually no 2-jolt differences, used in part 2
        twos += 1
        differs.append(2)
    else:
        threes += 1
        differs.append(3)
#print(ones)
#print(threes)
print("Part 1: ")
print("mult = " + str(ones*threes))

f.close()

print("part 2:")
print(differs)

# for part 2 we also keep track of how many 1's are in a row. Example:  1 1 1 3 1 1 , we would get 3, 2
groups = []
g = 1   # group counter, in example we'd have 2 groups of 1's
d = 0   # counter for each one in group
for l in range(len(differs)):
    if differs[l] == 1:
        d += 1
    else:   # move to next group
        groups.append(d)
        g += 1      # reset
        d = 0       # reset
print(groups)


while 0 in groups:   # Remove the 0's
    groups.remove(0)
print(groups)
"""
 To explain, 1 1 1 1 3 1 1 1 3 1 1 would result in 4 3 2.
When there are two 1-differences next to each other, there are __2__ options/permutations. 
    For ex. 3 4 5 is the sequence, so 1 1 are the two 1-differences. We could have 3 4 5 or 3 5.
When there are three 1-differences next to each other there are __4__ options/permutations
    For ex. 3 4 5 6 is the sequence. 1 1 1 . So options are 3 4 5 6, 3 4 6, 3 5 6 and 3 6
When there are four 1-differences there are __7__ options/permutations,
    Do the same pattern.
    Note that my program only goes up to 4x 1's in a row, would need to program or do the math for longer
"""

# Count all of the these
fourcount = groups.count(4)
threecount = groups.count(3)
twocount = groups.count(2)

# Then take the product of all of the permutations
product = (7 ** fourcount) * (4 ** threecount) * (2 ** twocount)

print("Final answer: " + str(product))  # Final answer

f.close()