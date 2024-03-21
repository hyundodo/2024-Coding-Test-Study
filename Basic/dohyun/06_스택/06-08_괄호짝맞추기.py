def solution(s):
    stack = []
    for element in s:
        if element == "(":
            stack.append(element)
        elif element == ")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True            
    
if __name__ == "__main__":
    s ="(())()"
    res = solution(s)
    print(res)