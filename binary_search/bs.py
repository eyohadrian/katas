import math

def search(nums, target):
    l,r= 0, len(nums) - 1

    while l <= r:
        m = r + l // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    return -1

assert search([-1,0,3,5,9,12], 9) == 4
assert search([-1, 2, 3], 9) == -1
assert search([-1, 2, 3, 9], 9) == 3
assert search([-1,0,3,5,9,12], 2) == -1
