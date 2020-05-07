方案一：
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

方案二：
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
