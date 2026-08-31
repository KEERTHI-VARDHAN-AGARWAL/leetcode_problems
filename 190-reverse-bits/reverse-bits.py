class Solution:
    def reverseBits(self, n: int) -> int:
        s=""
        while n>0:
            s=str(n%2)+s
            n//=2
        while len(s)<32:
            s='0'+s
        s=s[::-1]
        return int(s,2)