def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    ans_len = len(answers)
    ans_p1 = p1 * (ans_len // len(p1)) + p1[:ans_len % len(p1)]
    ans_p2 = p2 * (ans_len // len(p2)) + p2[:ans_len % len(p2)]
    ans_p3 = p3 * (ans_len // len(p3)) + p3[:ans_len % len(p3)]

    cor_count = [0,0,0]
    for idx, i in enumerate(answers):
        if i == ans_p1[idx]:
            cor_count[0] += 1
        if i == ans_p2[idx]:
            cor_count[1] += 1
        if i == ans_p3[idx]:
            cor_count[2] += 1
    
    answer = []
    highest = max(cor_count)
    for idx, j in enumerate(cor_count):
        if j == highest:
            answer.append(idx+1)
    return answer

if __name__ == '__main__':
    inputs = [1,3,2,4,2]
    res = solution(inputs)
    print(res)