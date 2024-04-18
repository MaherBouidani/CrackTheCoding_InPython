
'''
Given two inputs,

- First input is the location map, a 2D array
                  COL
          0   1   2   3   4       
      0 | O | E | E | E | X |
      1 | E | O | X | X | X |
ROW   2 | E | E | E | E | E |
      3 | X | E | O | E | E |
      4 | X | E | X | E | X |

    O = Robot, E = Empty, X = blocker

    location map {{'O','E','E','E','X'},{'E','O','X','X','X'},{'E','E','E','E','E'},{'X','E','O','E','E'},{'X','E','X','E','X'}}

- Second input is the query. It’s a 1D array consisting of distance to the closest blocker in the order from left, top, bottom and right
    [2, 2, 4, 1] 
    -> This means distance of 2 to the left blocker, 2 to the top blocker, 4 to the bottom blocker and 1 to the right blocker

Note : The location map boundary is also considered a blocker, meaning if the robot hits the boundary it also means it’s hitting the blocker.

Task: Write a function that takes these two inputs and returns the index of the robots (if any) that matches the query that we’re looking for.
Answer: [[1, 1]]

'''

# Helper Function
# def left_distance(start, end, row):
#     distance = 0

#     for index in range(start, end-1, -1):
#         if row[index] == 'X':
#             return start - index
#         else: 
#             distance += 1

#     return distance + 1

# def right_distance(start, end, row):
#     distance = 0

#     for index in range(start, end):
#         if row[index] == 'X':
#             return start - index
#         else: 
#             distance += 1

#     return distance + 1

        

    

# def top_distance():
#     pass


# def find_robot(location_map, query):

#     #left 
#     #top
#     #bottom
#     #right

#     for row_index, row in enumerate(location_map):

#         for col_index, col in enumerate(row):
#             if col == 'O':
#                 left = left_distance(col_index, 0, row)
#                 # top = col_distance(row_index, col_index, location_map, end=(0,col_index))
#                 # bottom = col_distance(row_index, col_index, location_map, end =(len(row)-1, col_index))
#                 right = right_distance(col_index, len(row), row)

#                 # if [left,top,bottom,right] == query:
#                 #     return [[row_index, col_index]]

#                 print((col_index,row_index),left, right)

#                 print("..................")
            

#     return 'no robots are found'



# location_map =  [['O','E','E','E','X'],['E','O','X','X','X'],['E','E','E','E','E'],['X','E','O','E','E'],['X','E','X','E','X']]
# query = [2, 2, 4, 1] 



# find_robot(location_map, query)


def findRobot(location_map, query):
    #left
    #top
    #bottom
    #right


    def left_distance(row_index, col_index):
        if location_map[row_index][col_index] == 'X' or col_index < 0:
            return 0 
        
        return 1 + left_distance(row_index, col_index - 1)
    

    def top_distance(row_index, col_index):
        if location_map[row_index][col_index] == 'X' or row_index < 0:
            return 0 
        
        return 1 + top_distance(row_index - 1, col_index)

    def bottom_distance(row_index, col_index):
        if location_map[row_index][col_index] == 'X' or row_index > len(location_map) - 1:
            return 0 
        
        return 1 + top_distance(row_index + 1, col_index)


    def right_distance(row_index, col_index):
        if location_map[row_index][col_index] == 'X' or col_index > len(location_map[0]) - 1:
            return 0 
        
        return 1 + right_distance(row_index, col_index + 1)




    for row_index, row in enumerate(location_map):
        
        for col_index, col in enumerate(row):

            if col == 'O':
                left = left_distance(row_index, col_index)
                top = top_distance(row_index, col_index)
                bottom = bottom_distance(row_index, col_index)
                right = right_distance(row_index, col_index)

                if [left, top, bottom, right] == query:
                    return [row_index, col_index]
                
    return 'no robots are found'

input_location_map = [['O','E','E','E','X'],['E','O','X','X','X'],['E','E','E','E','E'],['X','E','O','E','E'],['X','E','X','E','X']]
input_query =  [2, 2, 4, 1] 
print(findRobot(input_location_map, input_query))





    