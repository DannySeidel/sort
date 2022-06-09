list = [9, 5, 1, 3, 4, 8, 2, 7, 6]

for index, value in enumerate(list):
    while index > 0 and list[index - 1] > value:
        list[index] = list[index - 1]
        index -= 1

    list[index] = value

print(list)
