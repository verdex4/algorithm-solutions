import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    cur = 1
    for _ in range(t):
        n = int(data[cur])
        arr = list(map(int, data[cur + 1 : cur + 1 + n]))
        cur += n + 1

        k = [arr[0], arr[n - 1]].count(1)
        cnt = arr[1 : n - 1].count(0)

        if cnt >= k:
            print(k)
        else:
            print(-1)


solve()