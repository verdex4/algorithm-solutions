import math

def precompute() -> dict:
    ans = {} # x: лексикографически_первый_автомобильный_номер
    # количество_уникальных: номер
    letters = {1: "AAA", 2: "AAB", 3: "ABC"}
    numbers = {1: "000000", 2: "000001", 3: "000012", 4: "000123", 5: "001234", 6: "012345"}
    for k in range(1, 4):
        for m in range(1, 7):
            n = 10 - m
            # количество телефонных номеров x задается размещениями
            x = math.perm(n, k)
            l, nums = letters[k], numbers[m]
            # LDDDLLDDD, L - буквы, D - цифры
            license = l[0] + nums[:3] + l[1:] + nums[3:]
            ans[x] = license
    
    return ans
    

def solve():
    d = precompute()
    T = int(input())
    for _ in range(T):
        x = int(input())
        print(d.get(x, -1), flush=True)

solve()