问题描述：给一个数字，求该数字的平方根是多少？
参考链接：https://www.jianshu.com/p/d08dca8d1b56

方法一：
import math

math.sqrt( x )

方法二：二分法
def dichotomy_sqrt(n):
    if n > 1:   #在0到1之间的数，我们知道0到1之间的任何一个数平方后的结果都小于原值（0，1除外），因此如果要沿用上面的程序达不到“逼近”的作用，反而扩大了
        low = 1.0
        high = n
    else:
        low = n
        high = 1.0
    mid = (low + n)/2
    while abs(mid * mid - n) > 1e-6:
        if mid * mid > x:
            high = mid
            mid = (mid + low) /2
        else:
            low = mid
            mid = (mid + high) /2
    return mid

方法三：牛顿迭代法
#牛顿迭代法
def Newton_sqrt(x,y=1):
    z = x/y
    if abs(z - y) < 0.000001:
        return z
    else:
        y = (y + z)/2
        return Newton_sqrt(x,y)


