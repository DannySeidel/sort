list = [9, 5, 1, 3, 4, 8, 2, 7, 6]

length = len(list)
while (length > 1):
    limiter = 0
    for index in range(1, length):
        if list[index - 1] > list[index]:
            list[index], list[index - 1] = list[index - 1], list[index]
            limiter = index
    length = limiter

print(list)
