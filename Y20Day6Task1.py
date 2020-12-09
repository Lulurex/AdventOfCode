import numpy as np

# Set up read file
f = open("inputDec6.txt", "r")
raw = f.read().splitlines()
list = np.array(raw)
my_array = [y for y in list]
my_array = np.asarray(my_array) #create a numpy array

groupNum = 0
groupAnswers = []
yesAnswers = 0

#Read the whole lines
for i in range(len(my_array)):
    myLine = my_array[i]
    #print("array line: " + str(myLine))

    # if the line is empty
    if not my_array[i]:
        groupNum += 1

        #Empty the the array for the next group
        groupAnswers = []

    else:
        # For each character add if not in the group already
        for j in range(len(myLine)):

            if myLine[j] not in groupAnswers:
                groupAnswers.append(myLine[j])
                yesAnswers += 1

# groups complete:
print("groups processed:" + str(groupNum+1))
print("unique yes answers: " + str(yesAnswers))

totalYes = 0

f.close()
