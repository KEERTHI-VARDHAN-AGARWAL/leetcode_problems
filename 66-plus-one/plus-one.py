class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=0
        for i in digits:
            s=s*10+i
        s+=1
        a=[]
        while s>0:
            a.append(s%10)
            s//=10
        return a[::-1]

        