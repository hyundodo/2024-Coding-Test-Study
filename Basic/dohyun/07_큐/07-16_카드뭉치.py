from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else:
            break
    
    # if not goal:
    #     answer = "Yes"
    # else:
    #     answer = "No"
    return "Yes" if not goal else "No"

if __name__ == "__main__":
    cards1 = ["i", "drink", "water"]
    cards2 = ["want", "to"]
    goal = ["i", "want", "to", "drink", "water"]
    print(solution(cards1, cards2, goal))