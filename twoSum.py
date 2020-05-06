题目：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
一、暴力解法
解法一、如果默认只有两个这样的元素对
def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                return i, j
nums = [2, 7, 4, 5, 8, 10]
target = 9
i, j = twoSum(nums, target)
print(i, j)
输出结果是：
0,1


解法二、如果不只有这样的两个元素
output = []
def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                output.append([i, j])
    return output

nums = [2, 7, 4, 5, 8, 10]
target = 9
k = twoSum(nums, target)
print(k)
输出结果是：
[[0, 1], [2, 3]]


