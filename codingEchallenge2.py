def removeElement(nums, val) -> int:
    nums = [value for value in nums if value != val]
    k = len(nums)
    return k, f'nums={nums}'
    
    
print(removeElement([1,3,2,4,5,2,2],  2))