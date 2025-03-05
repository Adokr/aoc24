import re

def main():
    matrix = []
    with open("day4/input.txt", "r") as file:
        for line in file.readlines():
            matrix.append(list(line.strip('\n')))
    print(matrix)
    #return word_search(matrix)
    return day4part2(matrix)

def horizontal(line):
    tmp = "".join(line)
    x = re.findall(r"XMAS", tmp)
    y = re.findall(r"SAMX", tmp)
    return len(x) + len(y)

def vertical(matrix):
    count = 0
    columns = []
    for i in range(len(matrix[0])):
        tmp = []
        for j in range(len(matrix)):
            tmp.append(matrix[j][i])
        tmp = ''.join(tmp)
        columns.append(tmp)
    for column in columns:
        #print(column)
        count += len(re.findall(r"(XMAS)", column))
        count += len(re.findall(r"(SAMX)", column))
        #print(count)
    return count

def diagonal(matrix):
    count = 0
    diagonal_lines = ((len(matrix)+len(matrix[0])-1)*2)*[None]
    for k in range(0, len(matrix) + len(matrix[0]), 1):
        
        #print(len(diagonal_lines))
        for i in range(len(matrix)): #3*3
            for j in range(len(matrix[0])): #3*3
                if i+j == k:
                    if diagonal_lines[k] == None:
                        diagonal_lines[k] = matrix[i][j]
                    else:
                        diagonal_lines[k] += matrix[i][j]

    new_matrix = []
    for el in matrix:
        new_matrix.append(el[::-1])

    for k in range(0, len(new_matrix) + len(new_matrix[0]), 1):
        for i in range(len(new_matrix)): #3*3
            for j in range(len(new_matrix[0])): #3*3
                if i+j == k:
                    if diagonal_lines[k+(len(matrix)+len(matrix[0])-1)] == None:
                        diagonal_lines[k+(len(matrix)+len(matrix[0])-1)] = new_matrix[i][j]
                    else:
                        diagonal_lines[k+(len(matrix)+len(matrix[0])-1)] += new_matrix[i][j]
    print(diagonal_lines)
    for el in diagonal_lines:
        count += len(re.findall(r"(XMAS)", str(el)))
        count += len(re.findall(r"(SAMX)", str(el)))
    return count

def word_search(matrix):
    word_count = 0
    for i in range(len(matrix)):
        word_count += horizontal(matrix[i])
    word_count += vertical(matrix)
    word_count += diagonal(matrix)
    return word_count

def day4part2(matrix):
    count = 0
    surroundings = []
    for i in range(1, len(matrix)-1, 1):
        for j in range(1, len(matrix)-1, 1):
            if matrix[i][j] == 'A':
                surroundings = []
                surroundings.append([matrix[i-1][j-1],
                                     matrix[i+1][j-1],
                                     matrix[i+1][j+1],
                                     matrix[i-1][j+1]])
                if 'M' in surroundings[0] and 'S' in surroundings[0] and len(set(surroundings[0]))==2:
                    if (matrix[i-1][j-1] != matrix [i+1][j+1]) and (matrix[i+1][j-1] != matrix [i-1][j+1]):
                        count += 1
    return count
print(main())