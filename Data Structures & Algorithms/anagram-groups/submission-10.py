class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_map = {}
        solution = []
        index = 0
        for str in strs:
            count = tuple(str.count(chr(ord('a') + i)) for i in range(26))
            if count in dict_map:
                solution[dict_map[count]].append(str)
            else:
                list = [str]
                solution.append(list)
                dict_map[count] = index
                index += 1
            
        return solution