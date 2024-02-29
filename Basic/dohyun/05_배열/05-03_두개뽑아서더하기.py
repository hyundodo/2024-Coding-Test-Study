def solution(numbers):    
    answer = []
    for idx, i in enumerate(numbers[:-1]):
        for j in numbers[idx+1:]:
            answer.append(i+j)
    answer = answer.sort()
    return answer

if __name__ == '__main__':
    inputs = [2,1,3,4,1]
    res = solution(inputs)
    print(res)