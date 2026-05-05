class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length and reach the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Calculate effective rotation
        k = k % length
        if k == 0:
            return head

        # Step 3: Connect tail to head, making it circular
        tail.next = head

        # Step 4: Find the new tail (length - k - 1 steps from head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Step 5: New head is just after new tail; break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head