# linear pass using a map
# linear time and space complexity


def sortNums(nums):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    return ([1] * count.get(1, 0) +
            [2] * count.get(2, 0) +
            [3] * count.get(3, 0))

# One linear pass using three indices
# Linear Time complexity and in-place space complexity


def sortNums2(nums):
    one_index = 0
    three_index = len(nums) - 1
    index = 0
    while index <= three_index:
        if nums[index] == 1:
            nums[index], nums[one_index] = nums[one_index], nums[index]
            index += 1
            one_index += 1

        if nums[index] == 2:
            index += 1
        if nums[index] == 3:
            nums[index], nums[three_index] = nums[three_index], nums[index]
            three_index -= 1
    return nums


# Driver function
print(sortNums2([3, 3, 2, 1, 3, 2, 1]))
