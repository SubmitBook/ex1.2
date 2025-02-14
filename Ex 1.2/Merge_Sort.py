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

lst = [8, 3, 1, 7, 0, 10, 2]
sorted_lst = merge_sort(lst)
print(sorted_lst)
