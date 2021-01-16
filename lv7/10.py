# import sys
# input = sys.stdin.readline

# n = int(input())

# for _ in range(n):
#     word = input().strip()
#     lst = []

#     for i in word:
#         if i not in lst:
#             lst.append(i)
#         elif i != lst[-1]:
#             n -= 1
#             break

# print(n)

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    word = input().strip()
    for i in range(1, len(word)):
        if word.find(word[i - 1]) > word.find(word[i]):
            n -= 1
            break

print(n)
