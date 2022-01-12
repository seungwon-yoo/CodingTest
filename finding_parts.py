import sys

# 1. index 함수 이용
# 아 생각해보니까 있냐 없냐가 중요한거지 index가 중요한건 아니다.
# 그냥 if i in array: 이런 식으로 알아봐도 됨.
#######################################################
'''
N = int(input())
parts = list(map(int, sys.stdin.readline().split()))

M = int(input())
needs = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    try:
        parts.index(needs[i])
        print("yes", end=' ')
    except:
        print("no", end=' ')
'''
#######################################################

# 2. 이진 탐색 이용
#######################################################
'''
N = int(input())
parts = list(map(int, sys.stdin.readline().split()))
parts.sort()

M = int(input())
needs = list(map(int, sys.stdin.readline().split()))


def binary_search(array, need):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if need == parts[mid]:
            return mid
        elif need < parts[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None


for need in needs:
    result = binary_search(parts, need)
    if result is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
'''
#######################################################

# 3. 계수 정렬
#######################################################
N = int(input())
parts = list(map(int, sys.stdin.readline().split()))
array = [0] * 1000000

for part in parts:
    array[part] += 1

M = int(input())
needs = list(map(int, sys.stdin.readline().split()))

for need in needs:
    if array[need] != 0:
        print("yes", end=' ')
    else:
        print("no", end=' ')
