# 소트인사이드

N = int(input())

li = []

for i in str(N):
    li.append(int(i))
    
li.sort(reverse=True) # 내림차순 정렬

for i in li:
    print(i, end='') 