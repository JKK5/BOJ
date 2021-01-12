import sys

input = sys.stdin.readline
a, b, c = [int(input()) for _ in range(3)]
lst = list(str(a * b * c))

for i in range(10):
    print(lst.count(f'{i}'))
