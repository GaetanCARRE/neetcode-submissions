# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        slow, fast = head, head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:# deal if the lenght is even
                fast = fast.next
        
        right = self.reverseList(slow.next)
        slow.next = None
        left = head
        while right:
            tmp_left = left.next
            tmp_right = right.next
            left.next = right
            right.next = tmp_left
            left = tmp_left
            right = tmp_right 

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev