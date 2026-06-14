# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None
        
        # Reverse the first half while finding the middle with slow/fast pointers
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # 'prev' is head of reversed first half, 'slow' is head of second half
        max_sum = 0
        while slow:
            max_sum = max(max_sum, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return max_sum