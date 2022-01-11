import sys
import collections

N, M = map(int, input().split())

frame = list()
for _ in range(N):
    # 붙어있는 숫자 리스트로 변환
    frame.append(list(map(int, input())))

# (0,0)부터 시작. 구멍이 뚫려 있으면(0), 거기부터 dfs 시작.
# 0으로 연결된 부분을 세어 나가면서 1로 채움 -> 같은 곳을 다시 못 세도록.
# 재귀 구조 dfs 구현
count = 0


def dfs(x, y):
    if 0 <= x < N and 0 <= y < M and frame[x][y] == 0:
        frame[x][y] = 1
    else:
        return
    dfs(x + 1, y)
    dfs(x, y + 1)


for i in range(N):
    for j in range(M):
        if frame[i][j] == 0:
            count += 1
            dfs(i, j)

print(count)
