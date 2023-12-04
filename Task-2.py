from random import *

class input_error (Exception):
    pass

def input_guard(string):
    while True:
        try:
            variable = int(input(string))
            if variable < 2:
                    raise input_error
            break
        except ValueError:
             print('ERROR - 0!\nВведенно не целое число')
        except input_error:
             print('ERROR - 1!\nНе может быть меньше 2')
    return variable

def print_matrix(matrix):
    for line in matrix:
        for element in line:
            print(element, end=' ')
        print()

m = input_guard('Введите кол-во столбцов -> ')
n = input_guard('Введите кол-во строк -> ')

matrix = [[randint(-10,10) for _ in range(m)] for _ in range(n)]
print('Сгенерированная матрица MxN')
print_matrix(matrix)
for k in range(n-1):
    minimum = 10**10
    for i in range(k,n):
        for j in range(m):
            if matrix[i][j] < minimum:
                minimum = matrix[i][j]
                index = i
    matrix[k], matrix[index] = matrix[index], matrix[k]

print('Изменённая матрица')
print_matrix(matrix)