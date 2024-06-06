# Your solution to Exercise 26
n = input('')
lst = list(map(int, n.split()))
odd = []
even = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
even = even[::-1]
odd.sort()
output = even + odd
print(' '.join(map(str,output)))