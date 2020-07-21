# Solution to the Move Element To End problem

# Swapping allows for editing in place, however the rest of the elements may lose their
# natural order.
# Looks to be the case that we there's no way to swap w/o losing the original order

def move_element_to_end(arr, num):
    first = 0               # Pointer to the beginning of the array
    second = len(arr) - 1   # Pointer to the end of the array

    while first < second:
        if arr[second] == num:
            second -= 1
        
        else:
            if arr[first] == num:
                arr[first], arr[second] = arr[second], arr[first]
                second -= 1
                first += 1
            
            else:
                first += 1

if __name__ == "__main__":
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    num = 2

    move_element_to_end(array, num)
    print(array)

    assert array == [4, 1, 3, 2, 2, 2, 2, 2], "Not quite there yet."

    print("You're all set!")