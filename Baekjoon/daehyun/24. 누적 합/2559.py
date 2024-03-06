# 수열
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

result = []
result.append(sum(nums[:K]))

for i in range(N-K):
    result.append(result[i] - nums[i] + nums[K+1])

print(max(result))