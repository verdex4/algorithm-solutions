import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    cur = 1
    for _ in range(t):
        n = int(data[cur])
        arr = list(map(int, data[cur + 1 : cur + 1 + n]))
        cur += n + 1

        start = 0
        while start < n and abs(arr[start]) != 1:
            start += 1

        if start == n:
            print(*arr, sep=" ")
            continue
        if arr[start] == -1:
            arr[start] = 1

        pos = [start]
        for i in range(start + 1, n):
            if abs(arr[i]) == 1:
                pos.append(i)

        next_pos = 2
        for i in range(start + 1, n):
            if arr[i] == 1:
                next_pos += 1
            if arr[i] == -1:
                if next_pos < len(pos):
                    arr[i] = 0
                    next_pos += 1
                else:
                    arr[i] = 1

        print(*arr, sep=" ")

solve()