n, kol_rebra = map(int, input("").split(" "))
visited = [0 for _ in range(n)]
res = [50000 for _ in range(n)]


def BFS(n, spisok_smegnosty):
    res[0] = 0
    queue = [0]
    visited[0] = 1
    while len(queue) !=0:
        for vert in spisok_smegnosty[queue[-1]]:
            if visited[vert] == 0:
                queue = [vert] + queue
                res[vert] = res[queue[-1]]+1
                visited[vert]=1
        queue.pop(-1)
    return 0


spisok_smegnosty = {i: [] for i in range(n)}

for i in range(1, kol_rebra+1):
    rebro = list(map(int, input("").split(" ")))
    spisok_smegnosty[rebro[0]].append(rebro[1])
    spisok_smegnosty[rebro[1]].append(rebro[0])

BFS(n, spisok_smegnosty)
print(*res)