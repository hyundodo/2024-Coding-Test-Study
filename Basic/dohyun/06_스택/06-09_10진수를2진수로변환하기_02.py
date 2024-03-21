def solution(decimal):
    stack = []
    while decimal > 0:      # 끝까지 나눠서 몫이 0이 될 때까지 연산 수행
        remainder = decimal % 2
        stack.append(str(remainder))    # 여기서 문자열로 추가
        decimal //= 2
    
    binary = ''
    while stack:    # for 필요없이 while
        binary += stack.pop()
    
    return binary

if __name__ == "__main__":
    decimal = 12345
    res = solution(decimal)
    print(res)