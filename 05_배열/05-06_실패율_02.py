def solution(N, stages):
    
    # 도달한 사람 수
    arrive = [0]*(N+2) # 다 완료한 사람까지
    for stage in stages:    # stage 기준이 아닌 각 사람들의 stage 기준으로 간단히 만들 수 있음
        arrive[stage] += 1
        
    fail_rate = {}
    total_person = len(stages)
    
    # 실패율 구하기
    # 단 위에서 stage를 N+2로 했기 때문에, 명시적인 N 개의 stage만 사용
    for stage in range(1, N+1):
        if arrive[stage] == 0:
            fail_rate[stage] = 0
        else:
            fail_rate[stage] = arrive[stage] / total_person
        total_person -= arrive[stage]
    
    # 실패율에 따른 스테이지 반환 및 정렬
    answer = sorted(fail_rate, key=lambda x: fail_rate[x], reverse=True)

    return answer

if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages)) # [3,4,2,1,5]