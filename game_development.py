n, m = map(int, input().split())
A, B, d = list(map(int, input().split()))

maps = list()
for _ in range(n):
    maps.append(list(map(int, input().split())))

count = 1
stack = 0
maps[A][B] = 2
while True:
    if stack == 4:
        stack = 0
        if d == 0:
            A = A + 1
        elif d == 1:
            B = B - 1
        elif d == 2:
            A = A - 1
        else:
            B = B + 1
        if maps[A][B] == 1:
            break

    if d == 0:
        d = 3
        if maps[A][B - 1] == 0:
            maps[A][B - 1] = 2
            B = B - 1
            count += 1
            stack = 0
        else:
            stack += 1
    elif d == 1:
        d = 0
        if maps[A - 1][B] == 0:
            maps[A - 1][B] = 2
            A = A - 1
            count += 1
            stack = 0
        else:
            stack += 1
    elif d == 2:
        d = 1
        if maps[A][B + 1] == 0:
            maps[A][B + 1] = 2
            B = B + 1
            count += 1
            stack = 0
        else:
            stack += 1
    elif d == 3:
        d = 2
        if maps[A + 1][B] == 0:
            maps[A + 1][B] = 2
            A = A + 1
            count += 1
            stack = 0
        else:
            stack += 1
    print(A, B, d, stack)

print(count)
