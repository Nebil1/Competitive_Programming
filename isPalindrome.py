# 9
# solution 1, by converting to a string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num  = str(x)
        return num == num[::-1]
        
# without converthing to string 

def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False 
        
        inputNum = x
        newNum = 0

        while x > 0:
            newNum = newNum * 10 + x % 10 
            x = x // 10
        return newNum == inputNum