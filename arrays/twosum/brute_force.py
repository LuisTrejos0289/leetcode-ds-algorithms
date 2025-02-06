# Brute force, plain read using two loops, worst for O(N)

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

    sum = 0
    indexes = []

    for a, b in enumerate(nums):
        # Avoid any num higher than target
        if b > target:
            continue

        for c, d in enumerate(nums):
            if a == c:
                continue

            temp_sum = b + d

            if temp_sum == target:
                indexes.append(a)
                indexes.append(c)
                break

        # Meaning we only have one index and no match from second loop, so we re-start
        if len(indexes) == 2:
            break

    return indexes

resp = twoSum([2,7,11,15], 9)
print(resp)


            


        