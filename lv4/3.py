n = input().zfill(2)
old = n
cnt = 0

while True:
    sum = str(int(n[0]) + int(n[1]))
    n = n[-1] + sum[-1]
    cnt += 1

    if n == old:
        break

print(cnt)
