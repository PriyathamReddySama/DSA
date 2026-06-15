# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: a single-node list becomes empty after removing its only node
        if not head or not head.next:
            return None
        
        prev = None
        slow = head
        fast = head
        
        # Standard fast/slow pointer: fast moves twice as fast as slow.
        # When fast reaches the end, slow is at the middle node.
        # prev trails one step behind slow so we can unlink slow.
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Remove the middle node by skipping it
        prev.next = slow.next
        
        return head