import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    cur = 1
    for _ in range(t):
        n = int(data[cur])
        arr = list(map(int, data[cur + 1 : cur + 1 + n]))
        cur += n + 1

        odd = 0
        cnt0 = 0
        cnt2 = 0
        for x in arr:
            if x % 2 == 1:
                odd += 1
            elif x % 4 == 0:
                cnt0 += 1
            elif x % 4 == 2:
                cnt2 += 1

        res = max(odd, cnt0, cnt2)
        print(res)

solve()