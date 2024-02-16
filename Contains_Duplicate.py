def containsDuplicate(nums):
    hashset=set()
    for i in range(len(nums)):
        if nums[i] in hashset:
            return True
        hashset.add(nums[i])
    return False
