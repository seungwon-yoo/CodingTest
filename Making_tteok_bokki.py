import sys

N, M = map(int, sys.stdin.readline().split())

tteoks = list(map(int, sys.stdin.readline().split()))
tteoks.sort()

# 절단기에 설정할 높이는 from 0 to 제일 긴 떡의 길이
start, end = 0, max(tteoks)

result = 0
while (start <= end):
    # 총 얻은 떡의 길이
    total = 0

    mid = (start + end) // 2
    for tteok in tteoks:
        if tteok > mid:
            total += tteok - mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
