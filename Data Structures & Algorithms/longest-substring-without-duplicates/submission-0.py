class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        left = 0
        hashmap = {}
        for right in range(len(s)):
            char = s[right]

            while char in hashmap and hashmap[char]>=left:
                left = hashmap[char]+1
            hashmap[char] = right
            longest = max(longest,right-left+1)
        return longest
            