# Binary search, doesn't cover all test cases

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # Example
    # Target = 9
    # [2,7,11,15]
    # Index 0 and 1 should be returned since these positions match up to target

    indexes = []

    length = len(nums)

    index = abs(length // 2)

    indexes = listIndex(nums, 0, index, target)

    if not indexes:
        indexes = listIndex(nums, index, length, target)
    
    #Clause to evaluate full array
    if len(indexes) < 2:
         indexes = listIndex(nums, 0, length, target)
    
    return indexes

def listIndex(nums, start, length, target):
    indexes = []
    sum = 0
    for a, b in enumerate(nums[start:length]):
            sum+=b

            # Sum start index to get the actual index from nums array and not the zero based one
            curr_index = a + start

            if sum == target:
                indexes.append(temp_index)        
                indexes.append(curr_index)        

            temp_index = curr_index

    return indexes


resp = twoSum([3,2,3], 6)
print(resp)


            


        