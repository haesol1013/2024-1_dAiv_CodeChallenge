def pulling(matrix):
    while len(matrix) > 1:
        new_matrix = []
        for row in range(0, len(matrix), 2):
            new_row = []
            for col in range(0, len(matrix), 2):
                sum_ = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1]
                new_row.append(round(sum_/4, 1))
            new_matrix.append(new_row)
        matrix = new_matrix[:]
    return matrix[0][0]


size = int(input())
matrix = [[int(x) for x in input().split(" ")] for y in range(size)]
# matrix = [[-6, -8, 7, -4], [-5, -5, 14, 11], [11, 11, -1, -1], [4, 9, -2, -4]]
print(pulling(matrix))
