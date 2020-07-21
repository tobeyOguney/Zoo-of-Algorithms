# Solves the numbers in pi problem

# Consider all prefixes in pi_digits
# Then consider the correspoding suffixes as prefixes recursively
# Update the full word in memo to 1 + latter value

# O(n^3) time | O(n) space
def nums_in_pi(pi_digits, fav_nums, memo={}, first=0, second=None):
    if not second:
        second = len(pi_digits)
        memo = {(len(pi_digits), len(pi_digits)): -1}

    if first == second:
        return
    
    if (first, second) in memo:
        return

    for i in range(len(pi_digits[first:second])):
        prefix = pi_digits[first:second][:i+1]
        if prefix in fav_nums:
            _ = nums_in_pi(pi_digits, fav_nums, memo, first=first+i+1, second=second)

            memo[(first, second)] = min(memo.get((first, second), float('inf')), 1 + memo[(first+i+1, second)])
    
    return memo.get((first, second), -1)

# O(n^3) time | O(n^2) space
def get_fav_memo(pi_digits, fav_nums):
    # Implement memo table
    memo = [[False for _ in range(len(pi_digits))] for _ in range(len(pi_digits))]

    for i in range(len(pi_digits)):         # Iterate over rows
        for j in range(len(pi_digits)):     # Iterate over columns
            if pi_digits[i:j+1] in fav_nums:
                memo[i][j] = True
    
    # print(memo[0])     # Verify memo table

    return memo

# O(n^2) time | O(n^2) space
def dyn_nums_in_pi(pi_digits, fav_nums):
    is_fav = get_fav_memo(pi_digits, fav_nums)

    # Implement memo list
    memo = [float('inf') for i in range(len(pi_digits))]

    for i in range(len(memo)):
        if is_fav[0][i]:
            memo[i] = 0
        
        else:
            for j in range(1, i):
                if is_fav[j][i]:
                    if memo[j-1] != float('inf'):
                        memo[i] = min(memo[i], memo[j-1]+1)
                
    # print(memo)     # Verify  memo list

    return memo[-1] if memo[-1] != float('inf') else -1

if __name__ == "__main__":
    res = nums_in_pi(
        "3141592653589793238462643383279",
        {"314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"}
    )

    assert res == 2, res

    print("You're all set!")
