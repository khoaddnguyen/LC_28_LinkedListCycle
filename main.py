class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head  # example: slow = 1, fast = 2

        while fast and fast.next:  # not null
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
