import random

random.seed(4)

D=[]
for i in range(4):
    D.append([])
    for j in range(4):
        D[i].append(random.randint(1, 10))
print(D)
X = [D[i][i] for i in range(4)]
print(X)