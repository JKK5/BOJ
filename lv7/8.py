word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
t = 0

for x in word:
    for i in dial:
        if x in i:
            t += dial.index(i) + 3

print(t)
