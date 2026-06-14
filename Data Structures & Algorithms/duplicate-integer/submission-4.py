class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupl = set(nums)
        return len(dupl)!=len(nums)