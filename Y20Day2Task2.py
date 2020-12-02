import numpy as np

def get_line(wholeline):
    x = wholeline.split()
    b = x[0].split('-')
    y = b[0]
    z = b[1]
    q = x[1].replace(':', '')
    return y+z+q+x[2]

def get_min(wholeline):

    x = wholeline.split()
    b = x[0].split('-')
    y = b[0]
    return y

def get_max(wholeline):
    x = wholeline.split()
    b = x[0].split('-')
    y = b[1]
    return y

def get_letter(wholeline):
    x = wholeline.split()
    b = x[0].split('-')
    q = x[1].replace(':', '')
    return q

def get_password(wholeline):
    x = wholeline.split()
    return x[2]

#def check_password():
#    return 0;
# Set up read file
f = open("inputDec2.txt", "r")
raw = f.read().splitlines()
list = np.array(raw)
correct = 0

for i in range(0,1000):
    print("iteration: " + str(i))
    min = int(get_min(list[i]))
    max = int(get_max(list[i]))
    letter = get_letter(list[i])
    password = get_password(list[i])

    #print("minmax: " +password[min-1]+ password[max-1])
    #print("letter " + letter)

    first = letter == password[min-1]
    second = letter == password[max-1]
    #print(first)
    #print(second)
    if first ^ second:
        correct += 1
    #print("passwords correct: " + str(correct))

print("final passwords correct: "+ str(correct))


#password = get_line(list[1])
#print(password)

#for i in list:
#    print(i)

#print(list[1])

f.close()