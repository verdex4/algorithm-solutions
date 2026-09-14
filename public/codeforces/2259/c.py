import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))

    for _ in range(t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]

        first = 0
        while first < n and abs(arr[first]) != 1:
            first += 1
        if first == n:
            print(*arr, sep=" ")
            continue
        
        last = len(arr) - 1
        while last > 0 and abs(arr[last]) != 1:
            last -= 1

        arr[first] = 1
        arr[last] = 1

        for i in range(first + 1, last):
            if arr[i] == -1:
                arr[i] = 0

        print(*arr, sep=" ")

solve()