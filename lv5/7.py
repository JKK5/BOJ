import sys

input = sys.stdin.readline
c = int(input())

for _ in range(c):
    n, *lst = map(int, input().split())
    cnt = 0
    avg = sum(lst) / n

    for i in lst:
        if i > avg:
            cnt += 1

    print(f'{(cnt / n) * 100:.3f}%')
