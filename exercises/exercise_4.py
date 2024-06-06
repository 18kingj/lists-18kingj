# Your solution to Exercise 4
n = input('')
lst = list(map(int, n.split(',')))
odd_lst = [lst[num] for num in range(1, len(lst), 2)]
output = ','.join(map(str, odd_lst))
print(output)