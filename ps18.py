#/usr/bin/python3 
# Find the maximum total from top to bottom of the triangle in ps18.txt 

# extract triangle into a list of lists of each row of the triangle 

# import random 

# triangleFile = open('ps18.txt')

# # creates empty array 
# triangles = []
# for line in triangleFile.readlines():
#     row = line[:-1].split()
#     int_row = []
#     for elem in row:
#         int_row.append(int(elem))
#     triangles.append(int_row)

# triangleFile.close()

# tries = []

# for i in range(100000):
#     # implements a randomised algorithm  
#     max_total = 0 
#     # iterates through each row 
#     current_elem = triangles[0][0]
#     current_elem_row_index = 0 
#     max_total += current_elem
#     for row in triangles[1:]:
#         # possible indexes of elements adjacent to current element selected
#         possible_index_1 = current_elem_row_index
#         possible_index_2 = current_elem_row_index + 1

#         # values of elements with possible indexes 
#         value_1 = row[possible_index_1]
#         value_2 = row[possible_index_2]
 
#         if random.choice([True, False]):
#             # the value will be added to max_total 
#             max_total += value_1
#             # value will be current element and its index will be current elem index 
#             current_elem = value_1
#             current_elem_row_index = possible_index_1
#         else:    
#             max_total += value_2
#             current_elem = value_2
#             current_elem_row_index = possible_index_2
#     tries.append(max_total)        

# print(max(tries))        

# solution 

def compute():
	for i in reversed(range(len(triangle) - 1)):
		for j in range(len(triangle[i])):
			triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
	return str(triangle[0][0])


triangle = [  # Mutable
	[75],
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20, 4,82,47,65],
	[19, 1,23,75, 3,34],
	[88, 2,77,73, 7,63,67],
	[99,65, 4,28, 6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
	[ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23],
]


if __name__ == "__main__":
	print(compute())