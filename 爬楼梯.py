题目：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

不难发现，这个问题可以被分解为一些包含最优子结构的子问题，即它的最优解可以从其子问题的最优解来有效地构建，我们可以使用动态规划来解决这一问题。
第 ii 阶可以由以下两种方法得到：
在第 (i-1)阶后向上爬一阶。
在第 (i-2)阶后向上爬二阶。
所以到达第 i 阶的方法总数就是到第 (i-1) 阶和第 (i-2) 阶的方法数之和。
令 dp[i] 表示能到达第 i 阶的方法总数：
dp[i]=dp[i-1]+dp[i-2]
作者：LeetCode
链接：https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode/

def climbStairs(self, n: int) -> int:
        """
        爬到第n楼的方法，为爬到第n-1楼和n-2楼的方法之和
        因为爬到n-1楼后，再爬1楼就能到达n楼
        爬到n-2楼同理
        因此只需初始化爬到1楼和爬到2楼分别有多少种方法，便可以推导出爬到n楼的方法
        """
        fst = 1  # 爬到1楼只有1种方法
        scd = 2  # 爬到2楼有两种方法
        res = 0  # 初始化爬到n楼的方法
        for i in range(2, n):  # 从3楼开始算
            res = fst + scd
            
            fst = scd  # 推导下一层
            scd = res
        
        return max(n, res)  # 返回n和res中较大的那个

作者：antic-2
链接：https://leetcode-cn.com/problems/climbing-stairs/solution/pythondui-guan-fang-dong-tai-gui-hua-fa-geng-yi-do/
