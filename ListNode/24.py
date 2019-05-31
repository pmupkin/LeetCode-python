#这种方法在解法上有很多不必要的思考，设置一个计数，每次走两步就进行交换，实际上完全不需要设置计数，只需要交换当前节点和下一个节点，然后将当前节点指向交换完成后的下一个节点
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = head.next if head and head.next else head
        
        forward = ListNode(0)
        ffw = None
        count = 0
        while head:
            if count == 1:
                forward.next = head.next
                ffw.next = head
                ffw = ffw.next
                head = head.next
                ffw.next = forward
                count = 0
            else:
                count += 1
                ffw = forward
                forward = head
                head = head.next
        return res

#方法二，改进
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        res = head.next if head and head.next else head
        while head and head.next:
            a = head
            b = head.next
            pre.next, a.next, b.next = b, b.next, a
            head = head.next
            pre = a
        return res

#更进一步pre->a->b->b.next   ------> pre->b->a->b.next
class Solution:
    def swapPairs(self, head):
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next

