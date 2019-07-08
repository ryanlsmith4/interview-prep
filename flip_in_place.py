MATRIX1 = [[1,0]]
MATRIX2 = [[1,0,0],[0,0,1]]
MATRIX4 = [[1,2,3],[4,5,6],[7,8,9]]

def flip_vertical_axis(matrix):
    for list in matrix:
        print(list)
        list.reverse()
    return matrix

print(flip_vertical_axis(MATRIX2))