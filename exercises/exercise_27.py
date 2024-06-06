# Your solution to Exercise 27
n = int(input())
total = 0
for i in range(n):
    command = input()
    lst = command.split()
    if lst[0] == "D":
        total += int(lst[1])
    elif lst[0] == "W":
        total -= int(lst[1])
print(total)