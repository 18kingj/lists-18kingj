# Your solution to Exercise 3
n = input('')
lst = list(map(int, n.split()))
even_lst = [num for num in lst if num % 2 == 0]
output = ' '.join(map(str, even_lst))
print(output)
