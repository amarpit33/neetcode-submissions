class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in range(len(strs)):
            char = "".join(sorted(strs[i]))

            if char not in hashmap:
                hashmap[char] = []
            hashmap[char].append(strs[i])
        return list(hashmap.values())