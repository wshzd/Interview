def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_list = list(str(abs(x)))

        x_list.reverse()

        if x > 0:
            y = int(''.join(x_list))
        else:
            y = -(int(''.join(x_list)))

        if y < -(2 ** 31) or y > (2 ** 31 - 1):
            return 0

        return y

作者：shi-yue-40
链接：https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-shi-yue-40/
