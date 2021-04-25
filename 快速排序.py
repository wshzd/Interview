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
