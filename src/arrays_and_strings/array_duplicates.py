def remove_duplicates(nums) -> int:
    if len(nums) <= 1: return len(nums)

    start = end = 0

    while end < len(nums):
        if nums[start] == nums[end]:
            end += 1
        else:
            start += 1
            nums[start] = nums[end]
            
    
    return start + 1

test_1 = [1,1,2,2,3,3]
length = remove_duplicates(test_1)

assert length == 3