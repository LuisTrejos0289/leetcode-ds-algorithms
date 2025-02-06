# Do checks on incremental and decremental indexes

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # Exampleß
    # Target = 9
    # [2,7,11,15]
    # Index 0 and 1 should be returned since these positions match up to target

    indexes = []

    indexes = listIndex(nums, 0, target)
    
    return indexes

def listIndex(nums, start, target):
    sum = 0
    res = []

    length = len(nums) - 1

    if start == length:
        return res

    a=start
    for b in range(length, start-1, -1):
        if a == b:
            continue

        sum = nums[a] + nums[b]

        if sum == target:            
            return [a, b]
                
    res.extend(listIndex(nums=nums, start=start+1, target=target ))

    return res


            


        