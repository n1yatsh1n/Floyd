from math import inf

# заполнение матрицы смежности
m = [
    [0, 10, 18, 8, inf, inf],
    [10, 0, 16, 9, 21, inf],
    [inf, 16, 0, inf, inf, 15],
    [7, 9, inf, 0, inf, 12],
    [inf, inf, inf, inf, 0, 23],
    [inf, inf, 15, inf, 23, 0]
]
# размерность матрицы
n = 6
# матрица ответов
A = m

for k in range(n):
    for i in range(n):
        for j in range(n):
            m[i][j] = min(A[i][j], A[i][k] + A[k][j])
            m = A

for i in range(n):
    print(A[i])
