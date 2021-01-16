# def rev(str):
#     return int(''.join(reversed(str)))


# a, b = input().split()
# lst = [rev(a), rev(b)]
# print(max(lst))

a, b = input().split()

print(max(a[::-1], b[::-1]))
