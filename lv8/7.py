n = int(input())
ans = 0

for i in reversed(range(n // 5 + 1)):
    r = n - 5 * i

    if r % 3 == 0:
        ans = i + r // 3
        break

print(ans if ans else -1)
