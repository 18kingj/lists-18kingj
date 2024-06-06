# Your solution to Exercise 31
n = input()
lst = list(map(int, n.split()))
sum_lst = []
if len(lst) != 1:
    for i in range(len(lst)-1):
        sum_lst.append(lst[i-1] + lst[i+1])
    sum_lst.append(lst[len(lst)-2] + lst[0])
else:
    sum_lst.append(lst[0])
print(' '.join(map(str, sum_lst)))