#这个没什么难度，同时遍历两个链表，比较两个值的大小
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = helper = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
            
        res.next = l1 or l2
        
        return helper.next