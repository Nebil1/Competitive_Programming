class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while p.next:
            if p.next.next and p.next.val == p.next.next.val:
                z = p.next
                while z and z.next and z.val == z.next.val:
                    z = z.next
                p.next = z.next
            else:
                p = p.next
        return dummy.next