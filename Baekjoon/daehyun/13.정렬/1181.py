# # 단어 정렬

N = int(input())

words = [str(input()) for i in range(N)]

words = list(set(words)) # 집합자료형 
# print(words)
words.sort()
words.sort(key=len)

for i in words:
    print(i)
