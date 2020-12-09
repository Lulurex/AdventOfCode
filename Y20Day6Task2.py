import numpy as np

# Set up read file
f = open("inputDec6.txt", "r")
raw = f.read().splitlines()
list = np.array(raw)
my_array = [y for y in list]
my_array = np.asarray(my_array) #create a numpy array

groupie = 0         # which member within the group we're on
groupNum = 0        # which group we are on
groupAnswers = ""   # temporary storage to hold the possible unique unaminous letters
yesAnswers = 0      # running total of how many answer were unam yes


#Read the whole lines
for i in range(len(my_array)):
    myLine = set(my_array[i])
#    print("array line: " + str(myLine))

    # if the line is empty
    if not my_array[i]:
        yesAnswers += len(groupAnswers)

        #Empty the the array for the next group
        groupNum += 1
        groupAnswers = ""
        groupie = 0

    else:
        groupie += 1
        # check if its the first person in the group, if so add the whole line to groupAnswers
        if not groupAnswers and groupie == 1:
            groupAnswers = myLine

        else:  # Otherwise
            print("comparing ")
            print(groupAnswers)
            print(" to ")
            print(myLine)


            groupAnswers = set(groupAnswers).intersection(myLine) # find intersection
            print("answer is: ")
            print(groupAnswers)

        #check end of file
        if i == len(my_array)-1:
            yesAnswers += len(groupAnswers)


# groups complete:
print("groups processed:" + str(groupNum+1)) #498 groups
print("collective yes answers: " + str(yesAnswers))

f.close()
