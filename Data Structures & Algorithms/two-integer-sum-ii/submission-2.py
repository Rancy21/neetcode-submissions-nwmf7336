class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            num = numbers[i]
            diff = target - num

            if diff in d:
                return [d[diff] + 1, i + 1]
            d[num] = i


