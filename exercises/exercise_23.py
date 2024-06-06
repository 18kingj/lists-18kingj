# Your solution to Exercise 23
n = input('')
lst = list(map(int, n.split()))
lst.sort()
lst.reverse()
print(''.join(map(str, lst)))