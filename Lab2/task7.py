import random

def create_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        row = [random.randint(-10, 10) for _ in range(columns)]
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

n = 5
m = 6
matrix = create_matrix(n, m)

zero_rows = sum(1 for row in matrix if all(element == 0 for element in row))
print("Количество строк, содержащих нули:", zero_rows)

has_duplicate_rows = len(matrix) != len(set(tuple(row) for row in matrix))
print("Есть ли одинаковые строки в матрице:", has_duplicate_rows)

transposed_matrix = [[matrix[j][i] for j in range(n)] for i in range(m)]
print("Транспонированная матрица:")
print_matrix(transposed_matrix)

row_to_remove = int(input("Введите номер строки для удаления (от 1 до {}): ".format(n)))
column_to_remove = int(input("Введите номер столбца для удаления (от 1 до {}): ".format(m)))

if 1 <= row_to_remove <= n and 1 <= column_to_remove <= m:
    matrix.pop(row_to_remove - 1)
    for row in matrix:
        row.pop(column_to_remove - 1)
    print("Матрица после удаления строки {} и столбца {}:".format(row_to_remove, column_to_remove))
    print_matrix(matrix)
else:
    print("Неправильный номер строки или столбца. Удаление не выполнено.")

row_to_insert = int(input("Введите номер строки для вставки (от 1 до {}): ".format(n + 1)))
column_to_insert = int(input("Введите номер столбца для вставки (от 1 до {}): ".format(m + 1)))

if 1 <= row_to_insert <= n + 1 and 1 <= column_to_insert <= m + 1:
    new_row = [0] * m
    matrix.insert(row_to_insert - 1, new_row)
    for row in matrix:
        row.insert(column_to_insert - 1, 0)
    print("Матрица после вставки строки {} и столбца {}:".format(row_to_insert, column_to_insert))
    print_matrix(matrix)
else:
    print("Неправильный номер строки или столбца. Вставка не выполнена.")