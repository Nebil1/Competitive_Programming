class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
       List = []
       while head:
           List.append(head.val)
           head = head.next
       l, r = 0, len(List) - 1
       while l <= r:
            if List[l] != List[r]:
               return False
            l += 1
            r -= 1
       return True