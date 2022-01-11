import collections

N, M = map(int, input().split())

maze = list()
for _ in range(N):
    # 붙어있는 숫자 리스트로 변환
    maze.append(list(map(int, input())))

print(maze)

# count를 늘려가면서 진행하다가 제일 먼저 도달한 값의 count를 취함
# 맵이 넓어지면 비효율적일 것 같지만 일단 이렇게 함


def bfs(x, y):
    queue = collections.deque()
    queue.append((x, y, 1))

    while queue:
        x, y, count = queue.popleft()

        if x < 0 or x >= N or y < 0 or y >= M or maze[x][y] == 0:
            continue
        elif x == N-1 and y == M-1:
            return count

        queue.append([x - 1, y, count + 1])
        queue.append([x, y - 1, count + 1])
        queue.append([x + 1, y, count + 1])
        queue.append([x, y + 1, count + 1])


print(bfs(0, 0))
