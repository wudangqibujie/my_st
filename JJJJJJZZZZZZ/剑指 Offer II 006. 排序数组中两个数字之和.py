class Solution:
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers) - 1
        while i <= j:
            if (numbers[i] + numbers[j]) > target:
                j -= 1
            elif (numbers[i] + numbers[j]) < target:
                i += 1
            else:
                return [i, j]
        return

s = Solution()
numbers = [1,1, 1, 2, 2, 3]
target = 3
print(s.twoSum(numbers, target))