import sys

# 2 числа
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])

# строка
s = sys.stdin.read().strip()

# число + список
data = sys.stdin.read().split()
n = int(data[0])
arr = list(map(int, data[1:]))

# матрица n*m
data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
matrix = [list(map(int, data[i:i + m])) for i in range(2, 2 + n * m, m)]