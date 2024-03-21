from collections import deque

def solution(N, K):
    queue = deque(range(1, N+1))
    
    while len(queue) > 1:
        for _ in range(K-1): # K번째 요소 제거
            queue.append(queue.popleft())
            queue.popleft()
        
    return queue[0]

if __name__ == "__main__":
    N = 5
    K = 2
    print(solution(N, K))