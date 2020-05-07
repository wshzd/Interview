方案一：删除排序数组中的重复项
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

方案二：给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
        def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Initialize the counter and the array index.
        i, count = 1, 1
        
        # Start from the second element of the array and process
        # elements one by one.
        while i < len(nums):
            
            # If the current element is a duplicate, 
            # increment the count.
            if nums[i] == nums[i - 1]:
                count += 1
                
                # If the count is more than 2, this is an
                # unwanted duplicate element and hence we 
                # remove it from the array.
                if count > 2:
                    nums.pop(i)
                    
                    # Note that we have to decrement the
                    # array index value to keep it consistent
                    # with the size of the array.
                    i-= 1
                
            else:
                
                # Reset the count since we encountered a different element
                # than the previous one
                count = 1
           
            # Move on to the next element in the array
            i += 1    
                
        return len(nums)

作者：LeetCode
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/solution/shan-chu-pai-xu-shu-zu-zhong-de-zhong-fu-xiang-i-7/
