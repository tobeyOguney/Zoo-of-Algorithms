# Solution to the smallest difference problem

# Looks like the difference we're considering is absolute
# Pointer movement should ensure that this difference is a small as possible

# O(n lg n + m lg m) time | O(1) space
def smallest_difference(arr1, arr2):
    arr1.sort()
    arr2.sort()

    first = 0   # Pointer to arr1
    second = 0  # Pointer to arr2

    while first < len(arr1) and second < len(arr2):
        difference = abs(arr1[first] - arr2[second])

        if abs(arr1[first+1] - arr2[second]) < difference:
            first += 1
        
        elif abs(arr1[first] - arr2[second+1]) < difference:
            second += 1
        
        else:
            break
    
    return [arr1[first], arr2[second]]


if __name__ == "__main__":
    arr1 = [-1, 5, 10, 20, 28, 3]
    arr2 = [26, 134, 135, 15, 17]

    result = smallest_difference(arr1, arr2)

    assert result == [28, 26], "Not quite there yet."

    print("You're all set!")