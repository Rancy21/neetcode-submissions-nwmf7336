class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_map = {}
        for str in strs:
            count = tuple(str.count(chr(ord('a') + i)) for i in range(26))
            dict_map.setdefault(count, []).append(str)
            
        return list(dict_map.values())