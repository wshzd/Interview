题目：给定两个字符串str1和str2，len(str2）>len(str1)，判断str2是否包括str1中全排列的任何一个
本方法是用递归实现，使用全局变量count来记录全排列一共有
多少种。全局变量temp来记录排列中的状态。每次确定一个元素position变量记录当前排列元素的位置，然后在剩余元素s[s.index(i)+1:]+s[: s.index(i)]中继续进行全排列，直到剩余
元素个数为零，输出temp；然后回退temp// temp = temp[:position]，直到输出所有结果！

in_put = 'abcd'
temp = ''
count = 0


def order(s, position):
    global count
    global temp
    if len(s) == 0:
        print('out :', temp)
        count += 1
    else:
        for i in s:
            temp += i
            order(s[s.index(i) + 1:] + s[:s.index(i)], position + 1)
            temp = temp[:position]


order(in_put, 0)
print(count)

原文链接：https://blog.csdn.net/RobotM/article/details/105079739
