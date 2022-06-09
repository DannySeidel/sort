list = [5, 9, 1, 3, 4, 8, 2, 7, 6]

for count, _ in enumerate(list):
    buffer = count
    for index in range(count, len(list)):
        if list[buffer] > list[index]:
            buffer = index
    
    list[count], list[buffer] = list[buffer], list[count]
    
print(list)
