# 대표값2

x = [None] * 5

for i in range(5):
    x[i] = int(input())

x.sort()

print(int(sum(x)/5))
print(x[2])