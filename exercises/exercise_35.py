# Your solution to Exercise 35
n = input()
lst = list(map(int, n.split()))
num = lst.count(0)
for i in range(num):
    lst.remove(0)
    lst += [0]
print(' '.join(map(str, lst)))