#/usr/bin/python3 
# Find the maximum total from top to bottom of the triangle in ps18.txt 

# extract triangle into a list of lists of each row of the triangle 

import random 

triangleFile = open('ps18.txt')

# creates empty array 
triangles = []
for line in triangleFile.readlines():
    row = line[:-1].split()
    int_row = []
    for elem in row:
        int_row.append(int(elem))
    triangles.append(int_row)

triangleFile.close()

tries = []

for i in range(100000):
    # implements a randomised algorithm  
    max_total = 0 
    # iterates through each row 
    current_elem = triangles[0][0]
    current_elem_row_index = 0 
    max_total += current_elem
    for row in triangles[1:]:
        # possible indexes of elements adjacent to current element selected
        possible_index_1 = current_elem_row_index
        possible_index_2 = current_elem_row_index + 1

        # values of elements with possible indexes 
        value_1 = row[possible_index_1]
        value_2 = row[possible_index_2]
 
        if random.choice([True, False]):
            # the value will be added to max_total 
            max_total += value_1
            # value will be current element and its index will be current elem index 
            current_elem = value_1
            current_elem_row_index = possible_index_1
        else:    
            max_total += value_2
            current_elem = value_2
            current_elem_row_index = possible_index_2
    tries.append(max_total)        

print(max(tries))        

