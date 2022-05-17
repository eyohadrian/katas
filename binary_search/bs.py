import math

def search(nums, target):
    l=0
    r=len(nums) - 1
    index_target = -1

    while (l != r and nums[index_target] != target):
        if (nums[l] == target):
            index_target = l

        if (nums[r] == target):
            index_target = r

        if (nums[index_target] != target):
            m = math.floor((r + l) / 2)
            if (nums[m] == target):
                index_target = m
            elif (nums[m] > target):
                r = m
            elif (nums[m] < target):
                l = m

    return index_target


assert search([-1, 2, 3], 9) == 3
