# Your solution to Exercise 29
n = int(input())
count = 0
lst = [[0] for i in range(n)]
num = 1
for i in range(n):
    lst[0][i] = num
    num += 1
for i in range(1, n):
    lst[i][-1] = num
    num += 1
for i in range(n):
    lst[i]