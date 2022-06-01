nums = input().split("+")
nums = list(map(int, nums))
nums.sort()
if len(nums) <= 1:
    print(*nums)

else:
    print(*nums, sep="+", end="")
