#!/usr/bin/python3
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand 
# first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.

# What is the total of all the name scores in the file?

# obtaining names list from txt file 
namesFile = open('ps22_names.txt')
names = namesFile.read().split(',')
names = [name.strip('"') for name in names]
namesFile.close()

# sorting names in alphabetical order 
names.sort()

name_scores = 0 

for index in range(len(names)):
    
    name = names[index]

    alphabetical_position = index + 1 

    alphabetical_value = 0 
    for char in name:
        ascii_pos = ord(char)
        value = ascii_pos - 64 
        alphabetical_value += value 

    name_scores += (alphabetical_value*alphabetical_position)

print(name_scores)    
