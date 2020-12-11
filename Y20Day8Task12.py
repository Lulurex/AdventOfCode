import numpy as np
# https://adventofcode.com/2020/day/8

# Set up read file
f = open("inputDec8.txt", "r")
raw = f.read().splitlines()
MAX = len(raw)

#list = np.array(raw)
#my_array = [y for y in list]
#my_array = np.asarray(my_array) #create a numpy array


# Swap nop for jmp and vice versa
def Swap(text):
    if "nop" in text and text[5:] != 0:
        replacement = text.replace("nop", "jmp")
        return replacement
    if "jmp" in text and text[5:] != 0:
        replacement = text.replace("jmp", "nop")
        return replacement

# Check Loop is pulle from part 1 mostly. Check if there is an inf loop
def CheckLoop(changeid,max):


    Dict = set()    # Dict records the lines that have been seen before
    i = 0           # i is the line counter
    acc = 0         # acc is the running acc

    # Read the whole lines when applicable
    while i >= 0 and i <= (max - 1):
        line = raw[i]
        if i not in Dict:  # add line number when not in the set already
            Dict.add(i)
        else:       # if it was there, its a loop, end now
            print("Terminated early, accum is: " + str(acc))
            return False

        if "nop" in line and changeid == i:     # swap if we're changing this nop line
            rep = Swap(line)

            if "+" in rep:
                i += int(rep[5:])
            if "-" in rep:
                i -= int(rep[5:])
        if "nop" in line and changeid != i:     # do normal no operation
            i += 1

        if "acc" in line:                       # acc action
            if "+" in line:
                acc += int(line[5:])
                i += 1
            if "-" in line:
                acc -= int(line[5:])
                i += 1

        if "jmp" in line and changeid == i:     # jmp action if we're swapping here
            i += 1

        elif("jmp" in line and changeid != i):  # normal jmp action
            if "+" in line:
                i += int(line[5:])
            if "-" in line:
                i -= int(line[5:])
        else:
            pass


    if i > max:     # if we had i go too far out, False
        return False

    return acc      # Successful!

# iterate through the array and change a single nop or jmp action, and pass the line number
# for it to swap in the checkLoop function.
for j in range(len(raw)):
    text = raw[j]

    if "nop" in text and int(text[5]) != 0:     # If it's nop and not 0
        a = CheckLoop(j,MAX)                    # check if infinite
        if a != False:                          # not inf:
            print("end value: " + str(a))       # win win win
            break

    if "jmp" in text and int(text[5]) != 0:     # Same thing for jmp command
        a = CheckLoop(j,MAX)
        if a != False:
            print("end value: " + str(a))
            break

f.close()
