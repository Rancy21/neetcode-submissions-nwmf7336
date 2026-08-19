class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        l=0
        char_map = {}
        m = ""
        for r in range(len(s)):
            char = s[r]
            if not m:
                char_map[char] = 1
                m = 1                      
            elif char in char_map:
                char_map[char] += 1

                if char_map[char] > m:
                    m = char_map[char]
            else:
                char_map[char] = 1
                

            while  (r - l + 1 - m) > k:
                char_map[s[l]] -= 1
                l += 1
            
            
            max_length = max(max_length, r - l +1)
        return max_length
            

            




        