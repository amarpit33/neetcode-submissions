class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = []
        for dupl in nums:
            if dupl in num:
                return True
            num.append(dupl)
        return False
        