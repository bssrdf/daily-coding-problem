def find_min_max(nums):
    n = len(nums)
    if n%2 == 0:
        if nums[0] > nums[1]:
            mini, maxi = nums[1], nums[0]
        else:
            mini, maxi = nums[0], nums[1]
        i = 2
    else:
        mini = maxi = nums[0]
        i = 1
    while i < n-1:
        if nums[i] > nums[i+1]:
            if nums[i]   > maxi: maxi = nums[i]
            if nums[i+1] < mini: mini = nums[i+1]
        else:
            if nums[i+1] > maxi: maxi = nums[i+1]
            if nums[i]   < mini: mini = nums[i]
        i += 2
    return mini, maxi    


# Tests
assert find_min_max([4, 3, 1, 2, 5]) == (1, 5)
