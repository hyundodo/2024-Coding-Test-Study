# 부분합
# 연속된 수들의 부분합 중에서 가장 길이가 짧은 것

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))


start, end = 0, 0
length = 100001
sum = lst[0]

while start < end:
    if sum >= S:
        sum -= lst[start]
        length = min(length, end - start + 1)
        start += 1
    else:
        end += 1
        if end == N:
            break
        sum += lst[end]

if length == 100001:
    print(0)
else:
    print(length)