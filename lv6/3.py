def count(n):
    cnt = 0
    for x in range(1, n + 1):
        if x < 100:
            cnt += 1
        else:
            l = list(map(int, str(x)))
            if l[1] - l[0] == l[2] - l[1]:
                cnt += 1
    print(cnt)


n = int(input())
count(n)
