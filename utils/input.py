import sys
from itertools import islice


# ДАННЫЕ БЕЗ КОЛИЧЕСТВА РАУНДОВ t

# 2 числа
data = sys.stdin.read().split()
it = iter(data)
n, k = int(next(it)), int(next(it))

# 3 числа
data = sys.stdin.read().split()
it = iter(data)
n, k, m = int(next(it)), int(next(it)), int(next(it))

# строка
s = sys.stdin.read().strip()

# число + список
data = sys.stdin.read().split()
it = iter(data)
n = int(next(it))
arr = list(map(int, islice(it, n)))

# матрица m * n
data = sys.stdin.read().split()
it = iter(data)
m, n = int(next(it)), int(next(it))
matrix = [list(map(int, islice(it, n))) for _ in range(m)]


# ДАННЫЕ С КОЛИЧЕСТВОМ РАУНДОВ t

# 2 числа
data = sys.stdin.read().split()
it = iter(data)
t = int(next(it))
for _ in range(t):
    n, k = int(next(it)), int(next(it))

# 3 числа
data = sys.stdin.read().split()
it = iter(data)
t = int(next(it))
for _ in range(t):
    n, k, m = int(next(it)), int(next(it)), int(next(it))

# строка
data = sys.stdin.read().split()
it = iter(data)
t = int(next(it))
for _ in range(t):
    s = next(it)

# число + список
data = sys.stdin.read().split()
it = iter(data)
t = int(next(it))
for _ in range(t):
    n = int(next(it))
    arr = list(map(int, islice(it, n)))

# матрица m * n
data = sys.stdin.read().split()
it = iter(data)
t = int(next(it))
for _ in range(t):
    m, n = int(next(it)), int(next(it))
    matrix = [list(map(int, islice(it, n))) for _ in range(m)]