def solution(arr1, arr2):
    m, n = len(arr1), len(arr1[0])
    i, j = len(arr2), len(arr2[0])
    
    # for문 중첩해서 돌릴필요 없이, 간단하게 만들 수 있음.
    answer = [[0]*j for _ in range(m)]

    # 행렬 연산하듯이 arr2에서 열 고정하고 행을 움직여야 함. 바보같이 반대로 했었음.
    for idx_m in range(m):
        for idx_j in range(j):
            for idx_i in range(i):
                answer[idx_m][idx_j] += arr1[idx_m][idx_i] * arr2[idx_i][idx_j]   

    return answer

if __name__ == "__main__":
    arr1, arr2 = [[1, 4], [3, 2], [4, 1]], 	[[3, 3], [3, 3]]
    res = solution(arr1, arr2)
    print(res)