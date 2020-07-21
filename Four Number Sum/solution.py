# Solution to the four number sum problem

# What approach do we use here?

# We can't use pointer magic unless we sort
# since the input array is not necessarily in sorted order

# In the question, the solution were said to be okay in no particular order
# Hence, sorting is a possibility
# We only should not sort when there's a solution that can do better than O(nlg n) time
# Such a solution is highly non-trivial if it exists - hence its not my buisness to find it. LOL

# We sort first - in place
# Then we iterate over each element in a parent process
# Then we iterate over each child element in another process
# Then we use pointer magic to check if two other child elements yield a solution and return it

# O(n^3) time | O(n) space
def four_number_sum(lis, num):
    res = []

    lis.sort()

    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            diff = num - lis[i] - lis[j]

            if diff <= 0: continue

            first = j+1
            second = len(lis) - 1

            while first < second:
                sum_ = lis[first] + lis[second]

                if sum_ < diff:
                    first += 1

                elif sum_ > diff:
                    second -= 1

                elif sum_ == diff:
                    res.append([lis[i], lis[j], lis[first], lis[second]])
                    first += 1
                    second -= 1
    
    return res


if __name__ == "__main__":
    res = four_number_sum([7, 6, 4, -1, 1, 2], 16)

    assert res == [[7, 6, 4, -1], [7, 6, 1, 2]], res

    print("You're all set!")