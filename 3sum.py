


def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    results = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0 :
                results.append


numer = [-1,0,1,2,-1,-4]

print(threeSum(numer))