import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    # if n % h == 0:
    #     y = h
    #     x = n // h
    # else:
    #     y = n % h
    #     x = n // h + 1

    # print(y, str(x).zfill(2), sep='')

    y = n % h
    x = n // h + 1

    if y == 0:
        y = h
        x -= 1

    print(100 * y + x)
