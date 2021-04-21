"""
岛屿问题，求岛屿的数量
"""

grid = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


# 解法一：动态规划
def Island_num(arr):
    if not arr or not arr[0]:
        return 0
    N = len(arr)  # 行数
    M = len(arr[0])  # 列数
    res = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                res += 1
                dp(arr, i, j, N, M)
    return res


def dp(arr, i, j, N, M):
    if i < 0 or i > N or j < 0 or j > M or arr[i][j] != 1:
        return
    # 将上下左右为1的值全部改写为0
    arr[i][j] = 0
    dp(arr, i - 1, j, N, M)
    dp(arr, i + 1, j, N, M)
    dp(arr, i, j - 1, N, M)
    dp(arr, i, j + 1, N, M)


res = Island_num(grid)
print(res)
