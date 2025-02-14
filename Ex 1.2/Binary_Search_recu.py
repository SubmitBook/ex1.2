def binary_search_recursive(lst, target, left, right):

    mid = left + (right - left) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search_recursive(lst, target, left, mid - 1)
    else:
        return binary_search_recursive(lst, target, mid + 1, right)


lst = [3, 5, 7, 9]
target = 7
result = binary_search_recursive(lst, target, 0, len(lst) - 1)
print("The number of target is:", result)
