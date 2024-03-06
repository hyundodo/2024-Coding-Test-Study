# 커트라인

# 응시자의 수 N과 상을 받는 사람의 k
N, k = map(int, input().split())

# 각 학생의 점수x 입력
# x = list(map(int, input().split()))
# x.sort()

x = map(int, input().split())
x = sorted(x)
print(x[-k])