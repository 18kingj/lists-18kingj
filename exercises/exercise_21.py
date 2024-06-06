# Your solution to Exercise 21
n = input('')
lst = list(map(int, n.split()))
num1 = int(input(''))
num2 = int(input(''))
output = []
done = False
for num in range(len(lst)+1):
    if num == num1 and not done:
        output.append(num2)
        done = True
    else:
        if done:
            output.append(lst[num-1])
        else:
            output.append(lst[num])
print(' '.join(map(str, output)))