import numpy as np

# Set up read file
f = open("inputDec4.txt", "r")
raw = f.read().splitlines()
list = np.array(raw)
my_array = [y for y in list]
my_array = np.asarray(my_array) #create a numpy array

#Define the Person class
class Person:
    def __init__(self, eyr=None, byr=None, iyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.eyr = eyr
        self.byr = byr
        self.iyr = iyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def setValue(self, k, v):
        if k == "eyr":
            self.eyr = v
        if k == "byr":
            self.byr = v
        if k == "iyr":
            self.iyr = v
        if k == "hgt":
            self.hgt = v
        if k == "hcl":
            self.hcl = v
        if k == "ecl":
            self.ecl = v
        if k == "pid":
            self.pid = v
        if k == "cid":
            self.cid = v

    def validPassport(self):
        wrongLetters = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        eyeColors = ['blu', 'amb', 'brn', 'grn', 'gry', 'hzl', 'oth']
        digits = ['0','1','2','3','4','5','6','7','8','9']

        if (
                self.byr !=None and self.iyr != None and self.pid != None and self.eyr != None and self.ecl != None and self.hgt != None and self.hcl != None
        ):

            # for x in self.hcl
            if(int(self.byr) <= 2002 and int(self.byr) >= 1920 and len(self.byr) == 4):
                print("byr good")
            else:
                return False

            if(int(self.iyr) >= 2010 and int(self.iyr) <= 2020 and len(self.iyr) == 4):
                print("iyr good")
            else:
                return False

            if(int(self.eyr) >= 2020 and int(self.eyr) <= 2030 and len(self.eyr) == 4):
                print("eyr good")
            else:
                return False

            if(
                   ("cm" in self.hgt and int(self.hgt.replace('cm','')) >= 150 and int(self.hgt.replace('cm','')) <=193) or
                    ("in" in self.hgt and int(self.hgt.replace('in','')) >= 59 and int(self.hgt.replace('in','')) <= 76)
            ):
                print("hgt good")
            else:
                return False

            if(self.hcl.startswith('#') and len(self.hcl) == 7):
                for z in self.hcl:
                    if z in wrongLetters:
                        return False
                print("hcl good")
            else:
                return False

            if(self.ecl in eyeColors):
                print("ecl good")
            else:
                return False


            if(len(self.pid) == 9):
                for y in self.pid:
                    if(y not in digits):
                        return False
                print("pid good")
            else:
                return False


            return True

passportNum = 0
passport = []
# wash here
# make first person
passport.append(Person())
#Read the whole lines
for i in range(len(my_array)):

    #print("array line: " + str(my_array[i]))

    # Check to see if there's another person then create it
    # if the line is empty
    if not my_array[i]:
        passportNum += 1
        passport.append(Person())

    else:
        # Split the line
        myline = my_array[i].split()
        # print("split line: " + str(myline))

        # Read each pair in the line
        for j in range(len(myline)):
            myPair = myline[j].split(":")
            # print("pair: " + str(myPair))

            # Extract the Key and value from the person
            key = str(myPair[0])
            value = str(myPair[1])

            # Assign the key and value to the person
            passport[passportNum].setValue(key, value)

# Passports complete:
print("passports processed:" + str(passportNum+1))

validPassports = 0
# Find the passports that are valid


for i in range(passportNum+1):
    if passport[i].validPassport():
        validPassports += 1

print("valid passports: " + str(validPassports))
f.close()
