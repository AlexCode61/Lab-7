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

m = input_guard('Введите кол-во столбцов ->')
n = input_guard('Введите кол-во строк ->')

matrix = [[randint(-10,10) for _ in range(m)] for _ in range(n)]
maximum_summa = 0

for i in range(n):
    summa = 0
    for j in range(m):
        summa += matrix[i][j]
        print(matrix[i][j], end=' ')
    print('')
    if summa > maximum_summa:
        maximum_summa = summa
        index = i
print('Cтрока с максимальной суммой')
for element in matrix[index]:
     print(element, end=' ')
print()
print(f'Максимальная сумма - {maximum_summa}')