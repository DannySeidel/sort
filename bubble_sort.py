list = [9, 5, 1, 3, 4, 8, 2, 7, 6]

def bubble_sort_basic():
    length = len(list)
    swapped = False

    for _ in range(length - 1):
        for index in range(1, length):
            if list[index - 1] > list[index]:
                swapped = True
                list[index], list[index - 1] = list[index - 1], list[index]
        
        if not swapped:
            break

def bubble_sort_optimized():
    length = len(list)
    swapped = False

    for _ in range(length - 1):
        for index in range(1, length):
            if list[index - 1] > list[index]:
                swapped = True
                list[index], list[index - 1] = list[index - 1], list[index]
        
        length -= 1
        if not swapped:
            break

def bubble_sort_best():
    length = len(list)
    while (length > 1):
        limiter = 0
        for index in range(1, length):
            if list[index - 1] > list[index]:
                list[index], list[index - 1] = list[index - 1], list[index]
                limiter = index
        length = limiter

bubble_sort_best()
print(list)
