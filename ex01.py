# this function takes a list and an integer and return the indices of two numbers in the list that add up to the target number
# nums : list containing the numbers
# target : integer
def targetSum(nums, target):
    # we copy the content of the list so we don't override the indices
    numsCopy = nums[:]
    # we sort the copy
    numsCopy.sort()
    # we delete values greater than the target
    numsCopy = [x for x in numsCopy if x <= target]
    # we create all possible pairs to test them
    # it may be more efficent to start testing the possible pairs before finding them all
    numsPairs = [[numsCopy[x],numsCopy[y]] for x in range(len(numsCopy)) for y in range(len(numsCopy)) if y > x]
    # we search for the wanted pair
    for p in numsPairs:
        if sum(p) == target:
            # we return the indices of the two numbers that validate the condition
            # nums.index(p[0])+1 : we add this line to prevent the function from returning the same index for duplicate numbers
            return [nums.index(p[0]),nums.index(p[1],nums.index(p[0])+1)]
    else:
        # if none the pairs pass, we return an empty list
        return []



# an example list
myList = [1,2,4,5,9,7]
# an example target
# here 1 + 7 = 8
# index of 1 is 0 and index of 7 is 5
myTarget = 8
# expected result [0,5]
result = targetSum(myList,myTarget)

# we print the result
print("the result is",result)

# OUTPUT: the result is [0, 5]