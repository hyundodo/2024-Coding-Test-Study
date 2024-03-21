def solution(decimal):
    stack = []
    
    while decimal // 2:
        stack.append(decimal % 2)
        decimal = decimal // 2
    stack.append(decimal % 2)

    answer = ''
    for _ in range(len(stack)):
        answer += str(stack.pop())
        
    return answer

if __name__ == "__main__":
    decimal = 12345
    res = solution(decimal)
    print(res)