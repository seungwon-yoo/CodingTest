N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


"""
# A에서 N-K개의 가장 큰 수를 더함
# B에서 K개의 가장 큰 수를 더함
# 이렇게 하면 바꿔친거나 마찬가지

max_val = 0
max_val += sum(sorted(A, reverse=True)[:N-K])
max_val += sum(sorted(B, reverse=True)[:K])
print(max_val)

# 하지만 이렇게 하면 A에 더 큰 수가 있을 경우 잘못된 케이스가 발생함.
# ex
# A = [3,3,3,4]
# B = [1,2,3,4]
"""

# A는 오름차순 정렬, B는 내림차순 정렬
# K번 인덱스 0부터 비교해 나가다가 A에 있는 것이 더 크면 break
A.sort()
B.sort(reverse=True)

for i in range(K):
    if B[i] > A[i]:
        A[i] = B[i]
    else:
        break

print(sum(A))