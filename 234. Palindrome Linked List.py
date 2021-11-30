# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        record = []
        cur = head
        while cur:
            record.append(cur.val)
            cur = cur.next
           
        i, j = 0, len(record) - 1
        while i < j:
            if record[i] != record[j]:
                return False
            i += 1
            j -= 1
        
        return True
