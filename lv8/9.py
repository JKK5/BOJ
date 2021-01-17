import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    d = y - x
    moved = 1
    chk = 0
    res = 0

    while d > 0:
        d -= moved
        chk += 1

        if chk % 2 == 0:
            moved += 1

        res += 1

    print(res)
