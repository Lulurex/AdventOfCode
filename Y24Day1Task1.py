# Function to parse the text file
def parse_file(filename):
    firstlist = []
    secondlist = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                first_integer = int(parts[0])
                second_integer = int(parts[1])
                firstlist.append(first_integer)
                secondlist.append(second_integer)

    return firstlist, secondlist


# Example usage
filename = '2411test.txt'
firstlist, secondlist = parse_file(filename)
#print("First List:", firstlist)
#print("Second List:", secondlist)
firstlist.sort()
secondlist.sort()

'''Task 1
Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. 
For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; 
if you pair up a 9 with a 3, the distance apart is 6.'''
distance = 0

for i in range(0, len(firstlist), 1):
    equals = abs(firstlist[i]-secondlist[i])
    distance += equals
print("distance:")
print(distance)


'''Task 2
This time, you'll need to figure out exactly how often each number from the left list appears in the right list. 
Calculate a total similarity score by adding up each number in the left list 
after multiplying it by the number of times that number appears in the right list.
'''


firstset = set(firstlist)
secondset = set(secondlist)
intersectionset = firstset & secondset


res = {key: secondlist.count(key) for key in intersectionset}
#print(res)

fres = {key: firstlist.count(key) for key in intersectionset}
#print(fres)

similarity = {key: key * firstlist.count(key) * secondlist.count(key) for key in intersectionset}
#print(similarity)
print("similarity:")
print(sum(similarity.values()))