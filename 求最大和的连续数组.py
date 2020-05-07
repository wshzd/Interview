题目：给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # 下面为nums长度至少为2的情况
        res = nums[0]  # 先设定一个初始值（假设第一个数是可获得的最小值）
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])  # 更新后的nums[i]存储 以原始num[i]为结尾的子数组和的最大值
            res = max(res, nums[i])  # 更新最大值
        return res

作者：LotusPanda
链接：https://leetcode-cn.com/problems/maximum-subarray/solution/xiong-mao-shua-ti-python3-dong-tai-gui-hua-ji-hua-/
