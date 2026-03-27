class Subsets:
    def __init__(self, nums):
        self.nums = nums

    def get_subsets(self):
        n = len(self.nums)
        subsets = []
        # перебираем все числа от 0 до 2^n - 1
        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):  # проверяем, включён ли элемент
                    subset.append(self.nums[i])
            subsets.append(subset)
        return subsets

num = Subsets(list(map(int, input().split())))
print(num.get_subsets()) 