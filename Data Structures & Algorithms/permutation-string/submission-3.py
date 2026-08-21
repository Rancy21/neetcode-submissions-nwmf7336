class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        dic1 = {}
        dic2 = {}
        l = 0
        for char in s1:
            dic1[char] = 1 + dic1.get(char, 0)

        for r in range(len(s2)):
            char = s2[r]
            dic2[char] = 1 + dic2.get(char, 0)

            if char in dic1:
                if dic2[char] == dic1[char]:
                    if (r - l + 1) == len1:
                        return True
                elif dic2[char] > dic1[char]:
                    while dic2[char] > dic1[char]:
                        dic2[s2[l]] -= 1
                        l+=1
                
            else:
                while l <= r :
                    dic2[s2[l]] -= 1
                    l+=1
            
        return False



        