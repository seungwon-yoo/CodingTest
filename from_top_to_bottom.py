N = int(input())

nums = list()
for _ in range(N):
    nums.append(int(input()))

nums.sort(reverse=True)

for i in range(N):
    print(nums[i], end= ' ')