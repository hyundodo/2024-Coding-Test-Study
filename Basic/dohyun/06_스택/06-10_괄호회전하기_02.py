def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):  # 회전 with 인덱싱
        stack = []
        for j in range(n):  # 올바른 괄호 체크
            index = s[(i+j)%n]
            if index == "(" or index ==  "[" or index ==  "{":
                stack.append(index)
            else:
                if not stack:
                    break    # 해당 for문 정지
            
                if index == ")" and stack[-1] == "(":   # 스택 가장 마지막 것과 비교
                    stack.pop()
                elif index == "]" and stack[-1] == "[":
                    stack.pop()
                elif index == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    break
        
        else:                   # for문 다 돌면 실행 (무조건 다 돌아야지 정답이지!!)
            if not stack:       
                answer += 1
            
    return answer

if __name__ == "__main__":
    s = "}}}"
    res = solution(s)
    print(res)