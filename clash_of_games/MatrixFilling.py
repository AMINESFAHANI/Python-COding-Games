""""
Count the number of empty element in a N*N matrix with the one indexed x,y filling operation(Z)

"""

N, Z = list(map(int, input().split()))
M = [["" for _ in range(N)] for _ in range(N)]
nOfEmpty = N * N
r=[]
for i in range(Z):
    k = lambda x: int(x) - 1
    x, y = list(map(k, input().split()))

    for j in range(N):
        if not M[x][j]:
            M[x][j] = 1
            nOfEmpty -= 1
        if not M[j][y]:
            M[j][y] = 1
            nOfEmpty -= 1

    r.append(nOfEmpty)
print(*r,sep=", ")

