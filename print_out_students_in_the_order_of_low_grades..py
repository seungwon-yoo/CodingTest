N = int(input())

infos = list()
for _ in range(N):
    infos.append((input().split()))

infos.sort(key=lambda x: int(x[1]))

for i in range(N):
    print(infos[i][0], end=' ')
