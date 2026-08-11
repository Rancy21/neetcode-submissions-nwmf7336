class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_map = {}
        solution = []
        index = 0
        for str in strs:
            # count = tuple(str.count(chr(ord('a') + i)) for i in range(26))
            counts = [0] * 26
            for char in str:
                if 'a' <= char <= 'z':
                    counts[ord(char) - ord('a')] += 1

            count_tuple = tuple(counts)
            if count_tuple in dict_map:
                solution[dict_map[count_tuple]].append(str)
            else:
                list = [str]
                solution.append(list)
                dict_map[count_tuple] = index
                index += 1
            
        return solution