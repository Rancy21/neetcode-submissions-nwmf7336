class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        l=0
        char_map = {}
        m = 0
        for r in range(len(s)):
            char = s[r]
            char_map[char]= 1 + char_map.get(char, 0)

            if char_map[char] > m:
                m = char_map[char]
                

            while  (r - l + 1 - m) > k:
                char_map[s[l]] -= 1
                l += 1
            
            
            max_length = max(max_length, r - l +1)
        return max_length
            

            




        