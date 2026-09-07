import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    cur = 1

    ord_A = ord('A')
    ord_Z = ord('Z')

    for _ in range(n):
        s = str(data[cur]).strip()
        cur += 1

        res = s[0].lower()
        for j in range(1, len(s)):
            if ord_A <= ord(s[j]) <= ord_Z:
                res += "_" + s[j].lower()
            else:
                res += s[j]

        print(res, flush=True)
    

if __name__ == "__main__":
    solve()