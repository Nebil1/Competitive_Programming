class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
       result = 0
       c = Counter(nums)
       for i in c.keys():
           if i * 2 == k:
               result += c[i] // 2
           elif k - i in c:
                minValue = min(c[i],c[k-i])
                result += minValue
                c[i] -= minValue
                c[k-i] -= minValue
       return result