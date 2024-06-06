# Your solution to Exercise 7
n = input('')
lst = list(map(int, n.split()))
total = 0
for num in lst:
    total += num
print(total)