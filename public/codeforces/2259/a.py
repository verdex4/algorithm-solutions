import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    cur = 1
    for _ in range(t):
        n, k = int(data[cur]), int(data[cur + 1])
        s = str(data[cur + 2].strip())
        cur += 3

        cnt = 0
        for i in range(0, n, k):
            if all(s[j] == '1' for j in range(i, i + k)):
                cnt += 1
        print(cnt, flush=True)

solve()