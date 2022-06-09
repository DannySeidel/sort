array = [9, 5, 1, 3, 4, 8, 2, 7, 6]

def merge_sort(list):
    if len(list) <= 1:
        return list

    left = []
    right = []
    for index, value in enumerate(list):
        if index < len(list) // 2:
            left.append(value)
        else:
            right.append(value)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result.extend(left)
    if right:
        result.extend(right)

    return result

sorted_list = merge_sort(array)
print(sorted_list)
