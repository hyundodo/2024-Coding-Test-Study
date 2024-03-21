def solution(N, stages):
    
    # 도달한 사람 수
    arrive = []
    for stage in range(1, N+1):
        person_num = 0
        for person in stages:
            if person == stage:
                person_num += 1
        arrive.append(person_num)
    
    fail_rate = {}
    total_person = len(stages)
    
    # 실패율 구하기
    for idx, arrive_person in enumerate(arrive):
        if arrive_person == 0:
            fail_rate[idx+1] = 0
        else:
            fail_rate[idx+1] = arrive_person / total_person
        total_person -= arrive_person
    
    # 실패율에 따른 스테이지 반환 및 정렬
    answer = sorted(fail_rate, key=lambda x: fail_rate[x], reverse=True)

    return answer

if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages)) # [3,4,2,1,5]