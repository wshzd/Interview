def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.res = ""
        def helper(i,j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if len(self.res) < j - i -1 :
                self.res = s[i+1:j]
        for i in range(n):
            helper(i,i)
            helper(i,i+1)
        return self.res

作者：powcai
链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/duo-chong-si-lu-qiu-jie-by-powcai/
