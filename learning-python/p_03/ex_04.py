L = []
for i in range(8):
    L.append(2 ** i)
X = 5
if 2 ** X in L:
    print('at index', L.index(2 ** X))
else:
    print(X, 'not found')
