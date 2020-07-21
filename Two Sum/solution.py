# Solution to the Two Sum Problem

# I first thought of manipulating pointers to solve this problem.
# However, that will require that I sort the array.
# Not regarding that sorting limits the algorithms performance to o(nlg n),
# using this approach will require a solution that is less clean,
# because it messes with the indices.
# However, it will give the best time complexity O(nlg n).
# But, the space complexity will naively be O(n) which is not optimal.
# I can make the space complexity to be O(1) but it will require that I mutate the array.

# I think that a cleaner approach is to iterate over each number.
# > Totally ignoring numbers that are larger than or equal to the target.
# > Using linear search to determine if a number that matches the summative inverse w.r.t to the target
#   exists in the rest of the array. Further making its index available.
# > Returning a pair of the indices of the numbers that satisfy the requirements above, if such a pair exists.
# However, it will give the best space complexity O(1).
# But, the time complexity will be O(n^2)

# Since the array will not be used for further computation after the function call,
# I can go with the first solution, which will mutate the array.

# O(nlg n) time | O(1) space
def two_sum(nums, target):
    for i in range( len(nums) ):
        nums[i] = (nums[i], i)         # Storing original index for retrieval after sorting

    nums.sort(key=lambda num: num[0])   # Sort the array by the element first postion of the tuples in nums

    first = 0                 # Pointer moving into the array from the beginning
    second = len(nums) - 1    # Pointer moving into the array from the end

    result = []

    while first < second:
        sum_ = nums[first][0] + nums[second][0]
        
        if sum_ < target:
            first += 1
        
        if sum_ > target:
            second -= 1
        
        if sum_ == target:
            result = [ nums[first][1], nums[second][1] ]    # Get the original indices which were saved in the second postion of the tuples in nums
            break
    
    return result


if __name__ == "__main__":
    nums = [2, 11, 15, 7]
    target = 9
    result = two_sum(nums, target)
    assert result == [0, 3], "Not quite there yet"
    print("You're all set!")