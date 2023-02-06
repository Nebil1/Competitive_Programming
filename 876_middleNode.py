class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowPtr =  head
        fastPtr = head
        while (fastPtr and fastPtr.next):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        return slowPtr