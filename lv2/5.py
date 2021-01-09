# H, M = map(int, input().split())

# if M >= 45:
#     M -= 45
# else:
#     if H == 0:
#         H = 23
#     else:
#         H -= 1
#     M += 15

# print(H, M)

H, M = map(int, input().split())

time = 60 * H + M - 45

print(time // 60 % 24, time % 60)
