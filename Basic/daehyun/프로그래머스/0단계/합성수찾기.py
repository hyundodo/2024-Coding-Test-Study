# 합성수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120846

def solution(n):
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt > 2:
            answer += 1
    return answer