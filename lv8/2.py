n = int(input())
ans = 1
while n > 1:
    n -= 6 * ans
    ans += 1
print(ans)
