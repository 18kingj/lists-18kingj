# Your solution to Exercise 13
n = input('')
lst = list(map(int, n.split()))
total = 0
for num in lst:
    total += num
print(f'{total/len(lst): .2f}')