import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    for _ in range(t):
        x, y, k = int(next(it)), int(next(it)), int(next(it))

        res = 0
        i = 0
        while i <= y - 2 * x and i < k:
            res += (y + i) % (x + i)
            i += 1

        res += (k - i) * (y - x)
    
        print(res)

solve()