import sys

N = int(sys.stdin.readline()) # 점의 개수

lst = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y])

lst.sort()

for i in lst:
    print(i[0], i[1])
    
