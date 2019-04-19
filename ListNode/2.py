#整体思路还是很简单的，遍历链表，如果有进位就记录
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = cursor = ListNode(None)
        call = 0
        
        while l1 or l2 or call:
            s1 = s2 = 0
            if l1:
                s1 = l1.val
                l1 = l1.next
            if l2:
                s2 = l2.val
                l2 = l2.next
                
            call, a = divmod((s1+s2+call), 10)
            cursor.next = ListNode(a)
            cursor = cursor.next
        
        return res.next
		
#或者
class Solution:
	def addTwoNumbers(self, l1, l2):
		dummy = cur = ListNode(0)
		carry = 0
		while l1 or l2 or carry:
			if l1:
				carry += l1.val
				l1 = l1.next
			if l2:
				carry += l2.val
				l2 = l2.next
			cur.next = ListNode(carry%10)
			cur = cur.next
			carry //= 10
		return dummy.next