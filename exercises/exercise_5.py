# Your solution to Exercise 5
n = input('')
lst = list(map(int, n.split()))
output = []
for num in lst:
    if num not in output:
        output.append(num)
print(len(output))