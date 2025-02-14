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

def binary_search_recursive(lst, target, left, right):

    mid = left + (right - left) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search_recursive(lst, target, left, mid - 1)
    else:
        return binary_search_recursive(lst, target, mid + 1, right)

def merge_sort(lst):
    if len(lst) <= 1:
        return lst  # 递归终止条件

    mid = len(lst) // 2  # 找到中点
    left_half = merge_sort(lst[:mid])  # 递归排序左半部分
    right_half = merge_sort(lst[mid:])  # 递归排序右半部分

    return merge(left_half, right_half)  # 合并两个有序数组


def merge(left, right):
    sorted_lst = []  # 用于存放合并后的结果
    i = j = 0  # 双指针，分别指向 left 和 right 的起始位置

    # 逐个比较 left 和 right 数组中的元素
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # 选择较小的元素
            sorted_lst.append(left[i])
            i += 1
        else:
            sorted_lst.append(right[j])
            j += 1

    # 如果 left 还有剩余元素，全部添加到 sorted_lst
    sorted_lst.extend(left[i:])#extend，把列表拆开，逐个添加进新列表，区别于append

    # 如果 right 还有剩余元素，全部添加到 sorted_lst
    sorted_lst.extend(right[j:])

    return sorted_lst  # 返回合并后的有序数组

def quick_sort(lst):
    if len(lst) <= 1:
        return lst  # 递归终止条件

    pivot = lst[len(lst) // 2]  # 选择基准值（可以选第一个、中间或随机）

    left = [x for x in lst if x < pivot]  # 所有比 pivot 小的元素
    middle = [x for x in lst if x == pivot]  # 等于 pivot 的元素
    right = [x for x in lst if x > pivot]  # 所有比 pivot 大的元素

    return quick_sort(left) + middle + quick_sort(right)  # 递归排序并合并

#time measure
import time
import random

unsorted_lst = [random.randint(0, 1000000) for _ in range(100000)]
sorted_lst = merge_sort(unsorted_lst)

start_time = time.time()
merge_sort(unsorted_lst)
print("Merge Sort Time:", time.time() - start_time)

start_time = time.time()
quick_sort(unsorted_lst)
print("Quick Sort Time:", time.time() - start_time)

target = random.choice(sorted_lst)

start_time = time.time()
binary_search_iterative(sorted_lst, target)
print("Binary Search (sorted) Time:", time.time() - start_time)

start_time = time.time()
binary_search_iterative(unsorted_lst, target)
print("Binary Search (unsorted) Time:", time.time() - start_time)


