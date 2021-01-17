# import sys
# import math
# input = sys.stdin.readline

# a, b, v = map(int, input().split())
# ans = (v - a) / (a - b) + 1

# if (v - a) % (a - b) != 0:
#     ans = math.ceil(ans)
# else:
#     ans = round(ans)

# print(ans)

import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
ans = int((v - a) / (a - b)) + 1

if (v - a) % (a - b) != 0:
    ans += 1

print(ans)
