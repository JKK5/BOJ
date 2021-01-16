word = input().upper()
dct = {}

for i in word:
    if i not in dct:
        dct[i] = word.count(i)

freq = max(dct, key=dct.get)

# lst = [x for x, v in dct.items() if v == dct[freq]]
cnt = list(dct.values()).count(dct[freq])

# if len(lst) >= 2:
if cnt >= 2:
    print('?')
else:
    print(freq)
