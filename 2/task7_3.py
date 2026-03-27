class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find_pair(self):
        seen = {}
        for i, num in enumerate(self.nums):
            diff = self.target - num
            if diff in seen:
                return (seen[diff], i)
            seen[num] = i
        return None

arr = list(map(int, input().split()))
target = int(input())
result = TwoSum(arr, target)
print(result.find_pair())