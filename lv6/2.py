# def d(n):
#     d1 = n % 10
#     d2 = (n % 100) // 10
#     d3 = (n % 1000) // 100
#     d4 = n // 1000
#     return n + d1 + d2 + d3 + d4


# lst = list(range(1, 10001))

# for n in range(1, 10001):
#     n = d(n)
#     if n in lst:
#         lst.remove(n)

# for i in lst:
#     print(i)

def d(n):
    for i in str(n):
        n += int(i)
    return n


lst = list(range(1, 10001))

for n in range(1, 10001):
    n = d(n)
    if n in lst:
        lst.remove(n)

for i in lst:
    print(i)
