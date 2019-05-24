#删除倒数第n个节点，可以设置两个指针，一个前，一个后，前面的指针比后面的指针快n步，这样前面的走到末尾后，后面的正好相差n个
#比如说1->2->3->4->5, 删除倒数第2个，那么就是节点4，先让left指针走两步，到节点3，然后right开始走，这样left走到头
#即到节点5，这时候right到3，这里注意判断条件是right.next不为None，right前进n步后，需要判断一下，因为如果是倒数第五个
#那么这时候right就是None，删除第一个节点即可

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = right = head
        for _ in range(n):
            right = right.next
        if right is None: return head.next
        while right.next:
            left, right = left.next, right.next
        left.next = left.next.next
        return head