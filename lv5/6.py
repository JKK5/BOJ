import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    score = 0
    cnt = 0
    lst = input()

    for i in lst:
        if i == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
