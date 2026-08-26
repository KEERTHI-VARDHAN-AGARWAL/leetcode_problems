class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n={}
        for i in range(len(nums)):
            k=target-nums[i]
            if k in n:
                return [n[k],i]
            n[nums[i]]=i

        