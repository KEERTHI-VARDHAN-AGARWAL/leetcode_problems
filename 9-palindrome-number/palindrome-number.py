class Solution:
    def isPalindrome(self, x: int) -> bool:
        # sign =-1 if x<0 else 1
        # x=sign*x
        if x<0:
            return False
        elif str(x)==str(x)[::-1]:
            return True
        else:
            return False
        