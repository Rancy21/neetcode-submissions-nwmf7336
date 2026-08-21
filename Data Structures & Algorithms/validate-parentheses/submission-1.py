class Solution:
    def isValid(self, s: str) -> bool:
        char_list =[]
        for char in s:
            if not char_list:
                char_list.append(char)
                continue

            if char == '}':
                if char_list[-1] == '{':
                    char_list.pop()
                else:
                     return False
            elif  char ==']':
                if char_list[-1] == '[':
                    char_list.pop()
                else:
                    return False
            elif char == ')':
                if char_list[-1] == '(':
                    char_list.pop()
                else:
                    return False
            else:
                char_list.append(char)
            print(char_list)
        return True if len(char_list) == 0 else False
        