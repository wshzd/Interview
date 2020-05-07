题目：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
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
