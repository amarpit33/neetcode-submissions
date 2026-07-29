class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def backtrack(start,current):
            subset.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i+1,current)
                current.pop()
        backtrack(0,[])
        return subset