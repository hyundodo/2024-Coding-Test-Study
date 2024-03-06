# 좌표 정렬하기2
import sys
input = sys.stdin.readline

N = int(input())

lst = []

for i in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])

lst.sort(key=lambda lst: (lst[1], lst[0]))

for i in range(N):
    print(lst[i][0], lst[i][1])