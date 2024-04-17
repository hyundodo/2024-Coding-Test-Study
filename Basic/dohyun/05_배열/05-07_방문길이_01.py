def solution(dirs):
    move_ls = [(0,0)]
    for dir in dirs:
        if dir == "U":
            move_ls.append(tuple(sum(ele) for ele in zip(move_ls[-1], (0, 1))))
        elif dir == "D":
            move_ls.append(tuple(sum(ele) for ele in zip(move_ls[-1], (0, -1))))
        elif dir == "R":
            move_ls.append(tuple(sum(ele) for ele in zip(move_ls[-1], (1, 0))))
        elif dir == "L":
            move_ls.append(tuple(sum(ele) for ele in zip(move_ls[-1], (-1, 0))))

    only_move_ls = []   
    for move in move_ls:
        if move not in only_move_ls:
            if ((move[0] or move[1]) > -6) and ((move[0] or move[1]) < 6):
                only_move_ls.append(move)

    answer = len(only_move_ls)
        
    return answer

if __name__ == "__main__":
    dirs ="LULLLLLLU"
    res = solution(dirs)
    print(res)