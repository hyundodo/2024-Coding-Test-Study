# 두 수의 합

import sys
input = sys.stdin.readline

# 수열의 크기
n = int(input())

# 수열에 포함되는 수
lst = list(map(int, input().split()))

# x
x = int(input())

lst.sort()
start, end = 0, n-1
cnt = 0

while start < end:
    sum = lst[start] + lst[end]
    
    if sum == x:
        cnt += 1
        start += 1 # 그 다음 start 지점으로

    elif sum < x:
        start += 1 # 끝까지했는데 작으니까 다음 스타팅 포인트로
    else:
        end -= 1 # 너무 크니까 end 포인트를 바꿔서

print(cnt)
    