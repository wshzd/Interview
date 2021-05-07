#!/usr/bin/python
# encoding: utf-8


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkList:
    def __init__(self, head=None):
        self.head = head

    def get_head_node(self):
        """
        获取头部节点
        """
        return self.head

    def append(self, value):
        """
        从尾部添加元素
        """
        node = Node(value=value)
        cursor = self.head
        if self.head is None:
            self.head = node
        else:
            while cursor.next is not None:
                cursor = cursor.next

            cursor.next = node
            if value == 4:
                node.next = self.head

    def traverse_list(self):
        head = self.get_head_node()
        cursor = head
        while cursor is not None:
            print(cursor.value)
            cursor = cursor.next
        print("traverse_over")

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
       """
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


def main():
    l = LinkList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    head = l.get_head_node()
    print(l.hasCycle(head))
    # l.traverse_list()


if __name__ == "__main__":
    main()
