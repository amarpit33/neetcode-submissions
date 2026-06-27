class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        left = 0
        result = ""
        min_len = float('inf')
        need_freq,have_freq = {},{}
        have = 0

        for char in t:
            need_freq[char] = need_freq.get(char,0)+1
        need = len(need_freq)
        for right in range(len(s)):
            char = s[right]
            have_freq[char]= have_freq.get(char,0)+1

            if char in need_freq and need_freq[char]==have_freq[char]:
                have+=1
            while need==have:
                if (right-left+1)<min_len:
                    min_len = right-left+1
                    result = s[left:right+1]
                left_freq = s[left]
                have_freq[left_freq]-=1

                if left_freq in need_freq and have_freq[left_freq]<need_freq[left_freq]:
                    have-=1
                left+=1
        return result

                