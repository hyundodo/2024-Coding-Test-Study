from collections import deque

def solution(N, K):
    queue = deque([i for i in range(N)])
    
    while queue:
        for _ in range(K):
            queue.append(queue.popleft())
        if len(queue) == 1:
            answer = queue.popleft()
        else:
            queue.popleft()
        
    return answer

if __name__ == "__main__":
    N = 5
    K = 2
    print(solution(N, K))