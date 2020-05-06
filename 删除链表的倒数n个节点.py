一次遍历：指针b先走n步，然后指针a和b同时走，直到指针b走到链表末端
def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		# 增加一个特殊节点方便边界判断
		p = ListNode(-1)
		p.next,a,b = head,p,p
		# 第一个循环，b指针先往前走n步
		while n>0 and b:
			b,n = b.next,n-1
		# 假设整个链表长5，n是10，那么第一次遍历完后b就等用于空了
		# 于是后面的判断就不用做了，直接返回
		if not b:
			return head
		# 第二次，b指针走到链表最后，a指针也跟着走
		# 当遍历结束时，a指针就指向要删除的节点的前一个位置
		while b.next:
			a,b = a.next,b.next
		# 删除节点并返回	
		a.next = a.next.next
		return p.next	

作者：wang_ni_ma
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/dong-hua-yan-shi-19-shan-chu-lian-biao-de-dao-shu-/
