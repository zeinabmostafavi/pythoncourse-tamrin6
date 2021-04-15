import random
n = int(input("enter n: "))
m = int(input("enter m :"))
k = int(input("enter  k:"))

mt1 = [[random.randint(1, 10) for i in range(n)] for j in range(m)]
mt2 = [[random.randint(1, 10) for i in range(k)] for j in range(n)]
result = [[0 for i in range(len(mt2[0]))]for j in range(len(mt1))]

print("matrix1:")
for i in range(m):
    for j in range(n):
        print(mt1[i][j], end=' ')
    print()

print("matrix2:")
for i in range(n):
    for j in range(k):
        print(mt2[i][j], end=' ')
    print()

for i in range(m):
    for j in range(k):
        for h in range(n):
            result[i][j] += (mt1[i][h]*mt2[h][j])

print(result)
