n1 = int(input())
n2 = input()
rev = n2[::-1]

for i in range(len(rev)):
    print(n1 * int(rev[i]))

print(n1 * int(n2))
