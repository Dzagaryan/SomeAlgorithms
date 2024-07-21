n, kol_rebra = map(int, input("").split(" ") )
visited = [0 for i in range(n + 1)]


def DFS(n, key, spisok_smegnosty):
    for vert in spisok_smegnosty[key]:
        if visited[vert]==0:
            visited[vert] = 1
            DFS(n, vert, spisok_smegnosty)
    return 0


def SerchConnectivityComponentOfTheGraph(n, kol_rebra, spisok_smegnosty):
    kol = 0
    for vert in spisok_smegnosty.keys():
        suma = sum(visited)
        if visited[vert] == 0:
            visited[vert] = 1
            DFS(n, vert, spisok_smegnosty)
        if sum(visited) > suma:
            kol += 1
    return kol


spisok_smegnosty = {i: [] for i in range(1, n+1)}

for i in range(1, kol_rebra+1):
    rebro = list(map(int, input("").split(" ")))
    spisok_smegnosty[rebro[0]].append(rebro[1])
    spisok_smegnosty[rebro[1]].append(rebro[0])

print(SerchConnectivityComponentOfTheGraph(n, kol_rebra, spisok_smegnosty))