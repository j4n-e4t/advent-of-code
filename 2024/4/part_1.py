count = 0

with open("input.txt") as file:
    matrix = []
    for line in file:
        row = list(line.strip())
        matrix.append(row)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'X':

                # right
                if j <= len(matrix[0]) - 4:
                    if (matrix[i][j+1] == 'M' and
                        matrix[i][j+2] == 'A' and
                        matrix[i][j+3] == 'S'):
                        count += 1

                # left
                if j >= 3:
                    if (matrix[i][j-1] == 'M' and
                        matrix[i][j-2] == 'A' and
                        matrix[i][j-3] == 'S'):
                        count += 1

                # down
                if i <= len(matrix) - 4:
                    if (matrix[i+1][j] == 'M' and
                        matrix[i+2][j] == 'A' and
                        matrix[i+3][j] == 'S'):
                        count += 1

                # up
                if i >= 3:
                    if (matrix[i-1][j] == 'M' and
                        matrix[i-2][j] == 'A' and
                        matrix[i-3][j] == 'S'):
                        count += 1

                # diagonal down right
                if i <= len(matrix) - 4 and j <= len(matrix[0]) - 4:
                    if (matrix[i+1][j+1] == 'M' and
                        matrix[i+2][j+2] == 'A' and
                        matrix[i+3][j+3] == 'S'):
                        count += 1

                # diagonal down left
                if i <= len(matrix) - 4 and j >= 3:
                    if (matrix[i+1][j-1] == 'M' and
                        matrix[i+2][j-2] == 'A' and
                        matrix[i+3][j-3] == 'S'):
                        count += 1

                # diagonal up right
                if i >= 3 and j <= len(matrix[0]) - 4:
                    if (matrix[i-1][j+1] == 'M' and
                        matrix[i-2][j+2] == 'A' and
                        matrix[i-3][j+3] == 'S'):
                        count += 1

                # diagonal up left
                if i >= 3 and j >= 3:
                    if (matrix[i-1][j-1] == 'M' and
                        matrix[i-2][j-2] == 'A' and
                        matrix[i-3][j-3] == 'S'):
                        count += 1
print(count)
