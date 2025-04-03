
# You are given a 2D array of potentially unequal width and height. 0 in the matrix represent l and , 
# 1 in the matrix represent water horizontally and vertically. Write a function which returns the lengths of unique rivers.

# 0, 0, 0, 1
# 1, 1, 0, 0,
# 1, 0, 0, 1,
# 1, 0, 0, 1

# returns [1, 4, 2]

# 0, 0, 0, 1, 1,
# 1, 1, 0, 0, 1,
# 0, 0, 0, 1, 1,
# 0, 0, 0, 1, 0

# returns [6, 2]
matrix = [
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1]
]

def river_length(matrix):
    # if not matrix:
    #     return []
    
    rows, columns = len(matrix), len(matrix[0])

    #now to loop through the matrix

    for r in range(rows):
        for c in range(columns):
            if matrix[r][c]== 1:
                print (f"found water at : {r},{c}")
