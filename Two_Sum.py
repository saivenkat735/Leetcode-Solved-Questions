def twosum(num,target):
    prevmap={}
    for i,n in enumerate(nums):
        diff=target-n
        if diff in prevmap:
            return [prevmap[diff],i]
        prevmap[n]=i
    return 
