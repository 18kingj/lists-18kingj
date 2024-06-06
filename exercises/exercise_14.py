# Your solution to Exercise 14
n = input('')
lst = list(map(int, n.split()))
num = (lst[0]-lst[2])**2 + (lst[1]-lst[3])**2
print(f'{num**0.5: .2f}')