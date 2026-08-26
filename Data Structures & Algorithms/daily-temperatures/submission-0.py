class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0 for i in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            if i == 0:
                stack.append(i)
                continue

            temp = temperatures[i]

            while len(stack) > 0 and temp > temperatures[stack[-1]]:
                index = stack.pop()
                solution[index] = i - index
                
            stack.append(i)

        return solution
        