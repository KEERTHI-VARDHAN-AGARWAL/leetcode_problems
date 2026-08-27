class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=strs[0]
        for i in range(len(s)):
            for j in strs:
                if i>=len(j) or s[i]!=j[i]:
                    return s[:i]
        return s
