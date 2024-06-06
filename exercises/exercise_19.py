# Your solution to Exercise 19
n = input('')
lst = list(map(str, n.split('_')))
count = 0
for num in lst:
    lst[count] = num.capitalize()
    count += 1
print(''.join(lst))