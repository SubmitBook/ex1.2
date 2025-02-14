def binary_search_iterative(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

lst = [3, 5, 7, 9]
target = 7
result = binary_search_iterative(lst, target)
print("The number of target is:", result)
