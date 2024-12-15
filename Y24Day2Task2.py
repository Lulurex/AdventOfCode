''' Task 1
The engineers are trying to figure out which reports are safe.
The Red-Nosed reactor safety systems can only tolerate levels that are
either gradually increasing or gradually decreasing.
So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
'''

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

    return firstlist, secondlist, 