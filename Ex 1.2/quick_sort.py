def quick_sort(lst):
    if len(lst) <= 1:
        return lst  # 递归终止条件

    pivot = lst[len(lst) // 2]  # 选择基准值（可以选第一个、中间或随机）

    left = [x for x in lst if x < pivot]  # 所有比 pivot 小的元素
    middle = [x for x in lst if x == pivot]  # 等于 pivot 的元素
    right = [x for x in lst if x > pivot]  # 所有比 pivot 大的元素

    return quick_sort(left) + middle + quick_sort(right)  # 递归排序并合并


lst = [8, 3, 1, 7, 0, 10, 2]
sorted_lst = quick_sort(lst)
print(sorted_lst)
