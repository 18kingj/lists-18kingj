# Your solution to Exercise 24
n = input('')
n = n.replace(' 0', '')
lst = list(map(int, n.split()))
lst.sort()
lst.reverse()
print(' '.join(map(str, lst)))