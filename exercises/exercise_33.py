# Your solution to Exercise 33
n = input()
lst = [i for i in n]
if len(lst) == 3:
    first, second, last = lst
    if int(first+second) > int(second+last) and int(first+second) > int(first+last):
        print(first+second)
    elif int(second+last) > int(first+last):
        print(second+last)
    else:
        print(first+last)
elif len(lst) == 4:
    first, second, third, last = lst
    val1 = int(first+second+third)
    val2 = int(second+third+last)
    val3 = int(first+second+last)
    val4 = int(first+third+last)
    print(max(val1, val2, val3, val4))
    