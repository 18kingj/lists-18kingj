# Your solution to Exercise 25
size = int(input())
pattern = [["." for _ in range(size)]for _ in range(size)]
for i in range(len(pattern)):
    pattern[i][size//2] = "*"
for j in range(len(pattern)):
    pattern[size//2][j] = "*"
for row in range(size):
    for column in range(size):
        if row + column == size - 1:
            pattern[row][column] = "*"
for row, column in zip(range(size), range(size)):
    if row == column:
        pattern[row][column] = "*"  
for row in pattern:
    print(" ".join(row))
