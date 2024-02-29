def solution(answers):
    stud_answer = [
        [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
    ]
    
    scores = [0]*len(stud_answer)
    
    for idx, i in enumerate(answers):
        for stud, j in enumerate(stud_answer):
            if i == j[len(j) % idx+1]:
                scores[stud] += 1
                
    highest = max(scores)
    
    answer = []
    for stud, scor in enumerate(scores):
        if highest == scor:
            answer.append(stud)
            
    return answer

if __name__ == '__main__':
    inputs = [1,3,2,4,2]
    res = solution(inputs)
    print(res)