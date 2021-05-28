方法一：纯算法
lst = [11, 22, 33, 44, 55, 66, 77, 88, 99, 123, 234, 345, 456, 567, 678, 789]
n = 567
left = 0
right = len(lst)-1
count = 1
while left <= right :
    middle = (left +right)  // 2
    if n > lst[middle] :
        left = middle + 1
    elif n < lst[middle] :
        right = middle -1
    else :
        print(count)
        print("存在")
        print(middle)
        break
    count += 1
else :
    print("不存在")

方法二：递归
# lst = [11, 22, 33, 44, 55, 66, 77, 88, 99, 123, 234, 345, 456, 567, 678, 789]
def  binary_search(n,left,right):
    if left <= right :
        middle = (left+right) // 2
        if  n  <lst[middle] :
            right = middle -1
        elif n >lst[middle]:
            left = middle  + 1
        else :
            return middle
        return binary_search(n,left,right)  # 不加return返回永远是None
    else :
        return -1  #没有找到
 
 
print(binary_search(567,0,len(lst)-1)
    
方法三： 
def biinary_search(ls,target):
    left = 0
    right = len(ls) - 1
     if left > right:
        print("不不在这⾥里里")
    middle = (left + right) // 2
    if target < ls[middle]:
        return binary_search(ls[:middle], target)
    elif target > ls[middle]:
        return binary_search(ls[middle+1:], target)
    else:
        print("在这⾥里里")
binary_search(lst, 567)
    
    
    
    
