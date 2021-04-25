#!/usr/bin/python
# encoding: utf-8

"""
实现快速排序
"""

# 方法一：
quick_sort1 = lambda array: array if len(array) <= 1 else quick_sort(
    [item for item in array[1:] if item <= array[0]]) + [
                                                              array[0]] + quick_sort(
    [item for item in array[1:] if item > array[0]])


# 方法二：
def quick_sort(array):
    if not array or not array[0]:
        return array
    else:
        left_list = []
        right_list = []
        for i in range(1, len(array)):
            if array[i] <= array[0]:
                left_list.append(array[i])
            else:
                right_list.append(array[i])
        return quick_sort(left_list) + [array[0]] + quick_sort(right_list)


a = [1, 2, 6, 4, 8]
print(quick_sort(a))

# 方法三：
def quick_sort3(alist, start, end):
    """快速排序"""

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort3(alist, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort3(alist, low + 1, end)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort3(alist, 0, len(alist) - 1)
print(alist)


