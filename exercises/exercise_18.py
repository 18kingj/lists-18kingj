# Your solution to Exercise 18
n = input('')
lst = list(map(int, n.split()))
ma = max(lst)
mi = min(lst)
maxi = lst.index(ma)
mini = lst.index(mi)
lst[maxi], lst[mini] = mi, ma
print(' '.join(map(str, lst)))