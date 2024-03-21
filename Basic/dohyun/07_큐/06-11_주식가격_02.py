def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    stack = []
    for i in range(0, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    print(stack)
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
        
    return answer

if __name__ == "__main__":
    prices = [1,2,3,2,3]
    print(solution(prices)) # [4,3,1,1,0]