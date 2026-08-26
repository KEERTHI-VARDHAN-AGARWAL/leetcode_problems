class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans=""
        for i in range(len(s)):
            one=0
            for j in range(i,len(s)):
                if s[j]=='1':
                    one+=1
                if one == k:
                    sub=s[i:j+1]

                    if ans=="" or len(sub)<len(ans) or (len(sub)==len(ans)) and sub<ans:
                        ans=sub
                    break
                if one>k:
                    break
        return ans
        