class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        lastnode = head
        cur = head.next
        while cur:
            if lastnode.val <= cur.val:
                lastnode = lastnode.next
            else:
                pre = dummy
                while pre.next.val < cur.val:
                    pre = pre.next
                lastnode.next = cur.next
                cur.next = pre.next
                pre.next = cur            
            cur = lastnode.next
        return dummy.next
