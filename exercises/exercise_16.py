# Your solution to Exercise 16
n = input('')
lst = list(map(int, n.split()))
output = [str(num) for num in lst if lst.count(num) == 1]
print(' '.join(output))