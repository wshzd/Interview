方法一：
def reverseList1(self, head):
    """
    leetcode官方解法，思路和上一个解法大同小异，重点是在第1个节点前构造一个虚拟节点
    """
    if head is None or head.next is None:  # 兼容leetcode特殊用例，链表为空或只有1个节点
        return head
    pre_node = None
    current_node = head
    while current_node is not None:
        next_node = current_node.next
        current_node.next = pre_node
        pre_node = current_node
        current_node = next_node
    return pre_node
    
    
方法二：   
#!/usr/bin/env python
#coding = utf-8
class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next
 
def rev(link):
    pre = link
    cur = link.next
    pre.next = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre =cur
        cur = temp
    return pre
 
if __name__ == '__main__':
    link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
    root = rev(link)
    while root:
        print(root.data)
        root =root.next 
    
