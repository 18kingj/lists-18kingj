# Your solution to Exercise 36
n = input()
lst = list(map(int, n.split()))
num = int(input())
num_lst = []
for i in range(len(lst)):
    if lst[i] == num:
        num_lst.append(i+1)
if num_lst == []:
    print(None)
else:
    print(' '.join(map(str, num_lst)))