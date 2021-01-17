# import sys
# input = sys.stdin.readline

# a, b, c = map(int, input().split())

# try:
#     ans = int(a / (c - b)) + 1
#     if ans >= 0:
#         print(ans)
#     else:
#         print(-1)

# except ZeroDivisionError:
#     print(-1)

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if b < c:
    print(a // (c - b) + 1)
else:
    print(-1)
