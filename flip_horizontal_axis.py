TEST = [[1,2,3],[4,5,6],[7,8,9]]

TEST2 = [[1,0,0],[0,0,1]]

TEST3 = [[1]]

TEST4 = [[1,0,1],[1,0,1]]

# def flip_horizontal_axis(matrix):
#     # print([[7, 8, 9], [4, 5, 6], [1, 2, 3]])
#     new_list = []
#     for list in matrix:
#         # print(list[::-1])
#         new_list.append(list[::-1])
#     return new_list

# def flip_horizontal_axis(matrix):
#     # print([[7, 8, 9], [4, 5, 6], [1, 2, 3]])
#     return matrix[::-1]
    

def flip_horizontal_axis(matrix):
    rows = len(matrix) - 1
    columns = len(matrix[0]) - 1
    temp = 0
    i = 0
    while i <= rows/2:
        j = 0
        while j <= columns:
            temp = matrix[i][j]
            matrix[i][j] = matrix[rows - i][j]
            matrix[rows - i][j] = temp
            j = j + 1
    i = i + 1
            


if __name__ == "__main__":
    print(flip_horizontal_axis(TEST3))