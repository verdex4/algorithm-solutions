def solve():
    p, q = map(int, input().split(" "))
    if p == 0:
        print("2", flush=True)
    else:
        print("1", flush=True)
    
    p1, q1 = map(int, input().split(" "))
    if q == q1:
        print("c", flush=True)
    else:
        print("r", flush=True)

solve()