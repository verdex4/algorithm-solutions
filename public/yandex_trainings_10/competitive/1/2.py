import sys
from collections import Counter

def solve():
    data = sys.stdin.read().split()
    s = data[0].strip()
    t = data[1].strip()

    i = 0
    cnt = Counter(t)
    res = 0

    for j in range(len(s)):
        if s[j] not in cnt:
            for k in range(i, j):
                cnt[s[k]] += 1
            i = j + 1
            continue

        while cnt[s[j]] == 0:
            cnt[s[i]] += 1
            i += 1

        res += j - i + 1
        cnt[s[j]] -= 1

    print(res)

if __name__ == '__main__':
    solve()