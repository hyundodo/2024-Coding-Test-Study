# 좌표계 검증
def validation(nx, ny):
    if (0 <= nx < 11) and (0 <= ny < 11):
        return nx, ny

# 좌표이동
def moving(nx, ny, dir):
    if dir == "U":
        ny += 1
    elif dir == "D":
        ny -= 1
    elif dir == "R":
        nx += 1
    elif dir == "L":
        nx -= 1
    return nx, ny

# 실행
def solution(dirs):
    x, y = 5, 5
    answer_ls = set()   # 이동 저장할 때 중복 제거
    for dir in dirs:
        nx, ny = moving(x, y, dir)
        if not validation(nx, ny):
            continue
        answer_ls.add((nx, ny, x, y))   # set은 add로 추가
        answer_ls.add((x, y, nx, ny))
        x, y = nx, ny
    answer = len(answer_ls) / 2
    
    return answer

if __name__ == "__main__":
    dirs ="LULLLLLLU"
    res = solution(dirs)
    print(res)