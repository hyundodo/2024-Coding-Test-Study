def solution(arr1, arr2):
    m, n = len(arr1), len(arr1[0])
    i, j = len(arr2), len(arr2[0])
    
    answer = [[] for r in range(m)]

    for row in range(m):
        for col in range(j):
            answer[row].append(0)
    print(answer)
    
    for idx_m in range(m):
        for idx_i in range(i):
            for idx_j in range(j):
                answer[idx_m][idx_i] += arr1[idx_m][idx_j] * arr2[idx_j][idx_i]   
                
    return answer

if __name__ == "__main__":
    arr1, arr2 = [[1, 4], [3, 2], [4, 1]], 	[[3, 3], [3, 3]]
    res = solution(arr1, arr2)
    print(res)