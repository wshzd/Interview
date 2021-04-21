# 返回有序数组中目标值第一次出现的索引，如果没有就返回-1

def findFirstIndex(array, x):
    if len(array) < 1 or array[-1] < x:
        return -1
    else:
        low = 0
        high = len(array)
        while low < high:
            mid = low + (high - low)//2
            if array[mid] == x:
                return mid
            elif array[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return -1

array = [0, 0, 0, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5]
x = 5
index = findFirstIndex(array, x)
print(index)
