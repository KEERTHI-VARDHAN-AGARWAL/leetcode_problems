class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        a=nums
        a.append(target)
        a.sort()
        return a.index(target)