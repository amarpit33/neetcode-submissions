class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for c in range(len(nums)):
            needed = target - nums[c]
            if needed in count:
                return [count[needed],c]
            count[nums[c]]=c
