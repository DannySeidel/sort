array = [9, 5, 1, 3, 4, 8, 2, 7, 6]

def quicksort(list, low, high):
    if low >= high or low < 0:
        return None

    p = partition(list, low, high)

    quicksort(list, low, p - 1)
    quicksort(list, p + 1, high)

def partition(list, low, high):
    pivot = list[high]
    i = low - 1

    for j in range(low, high):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]

    i += 1
    list[i], list[high] = list[high], list[i]

    return i

quicksort(array, 0, len(array) - 1)
print(array)