def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while(i != len(nums)):
            if nums[i] in nums[i+1:]:
                del nums[i]
            else: 
                i += 1
        return len(nums)

作者：Ethan0928
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/ji-jian-qi-xing-pythondai-ma-jie-jue-by-ethan0928/
