def solution(s):
    s_ls = []
    for ele in s:
        s_ls.append(ele)
    
    stack = []
    answer = 0
    for _ in range(len(s)):
        s_ls.append(s_ls.pop())
        
        for s_ls_ele in stack:
            if s_ls_ele == ("[" or "(" or "{"):
                stack.append(s_ls_ele)
            elif s_ls_ele == ("]" or ")" or "}"):
                if not stack:
                    continue
                else:
                    stack.pop()
                    answer += 1
    return answer

if __name__ == "__main__":
    s = "[](){\}"
    res = solution(s)
    print(res)