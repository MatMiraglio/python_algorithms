def removeElement(nums, val: int) -> int:

    swapIndex = 0

    for i, numb in enumerate(nums):
        if numb == val:
            temp = nums[swapIndex]
            nums[swapIndex] = numb
            nums[i] = temp
            swapIndex += 1

    while nums and nums[0] == val:
        del nums[0]

    return len(nums)


data = [0, 1, 2, 2, 3, 0, 4, 2]

print(removeElement([1], 1))

print(removeElement(data, 2))
print(data)
