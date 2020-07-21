# Solution to the Triplet Sums problem

# Since the array will not be used for further computation, we can sort it in place.
# Doing this enables me to manipulate pointers to enumerate the solutions.

def triplet_sums(arr, target):
    arr.sort()

    results = []

    for i in range( len(arr) ):
        j = i+1
        k = len(arr) - 1

        while j < k:
            sum_ = arr[i] + arr[j] + arr[k]
            if sum_ < target:
                j += 1
            
            elif sum_ > target:
                k -= 1
            
            else:
                results.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
    
    return results


if __name__ == "__main__":
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    target = 0

    results = triplet_sums(array, target)

    print(results)