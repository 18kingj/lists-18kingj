# Your solution to Exercise 28
n = input()
lst = list(map(int, n.split()))
num = lst.pop(0)
print(num)
print(' '.join(map(str, lst)))