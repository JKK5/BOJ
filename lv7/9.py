s = input()
n = len(s)
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in lst:
#     cnt = s.count(i)
#     if cnt:
#         n -= 1 * cnt

for i in lst:
    n -= s.count(i)

print(n)
