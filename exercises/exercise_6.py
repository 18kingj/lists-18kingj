# Your solution to Exercise 6
n = input('')
lst = list(map(int, n.split()))
count = 0
pre = lst[0]
for num in range(1, len(lst)-1):
    if lst[num] > pre and lst[num] > lst[num + 1]:
        count += 1
    pre = lst[num]
print(count)