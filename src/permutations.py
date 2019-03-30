def permute(nums):
    res = []
    DBS(nums, [], res)
    return res

def DBS(nums, path, res):
    if not nums:
        res.append(path)
    else:
        for i, num in enumerate(nums):

            DBS( nums[:i] + nums[i + 1 :], path + [num], res)


test = [1,2,3]
result = permute(test)
print(result)