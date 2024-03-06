# 수 정렬하기 3

"""
# 메모리 부족

N = int(input())
x = [None] * N

for i in range(N):
    x[i] = int(input())

# print('수 입력 완료')

for j in range(N):
    print(x[j])

"""

import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * 10001 # 각 수의 등장 횟수를 저장하기 위한 리스트. 10,000 이하인 자연수라는 조건

for _ in range(N):
    num = int(input())
    lst[num] += 1 

for i in range(10001):
    if lst[i]:
        for j in range(lst[i]):
            print(i)

