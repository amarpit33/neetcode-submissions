class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        have = {}
        left = 0

        for char in s1:
            need[char] = need.get(char,0)+1
        
        for right in range(len(s2)):
            char = s2[right]

            have[char] = have.get(char,0)+1

            if (right-left+1)==len(s1):
                if have == need:
                    return True
                have[s2[left]]-=1
                if have[s2[left]]==0:
                    del have[s2[left]]
                left+=1
        return False

