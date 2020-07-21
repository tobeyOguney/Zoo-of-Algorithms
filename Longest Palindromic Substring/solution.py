# Solves the longest palindromic substring problem

# O(n^2) time | O(1) space
def long_palind_sub(string_):
    palinds = None

    for i in range(1, len(string_)):
        first = i-1
        second = i if string_[i] == string_[i-1] else i+1

        counter = 0
        while first >= 0 and second < len(string_) and string_[first] == string_[second]:
            counter += 1
            first -= 1
            second += 1
    
        if counter:
            if not palinds:
                palinds = [second - first - 1, [first+1, second-1]]
            if second-first-1 > palinds[0]:
                palinds = [second - first - 1, [first+1, second-1]]

    if palinds:
        return string_[palinds[1][0] : palinds[1][1]+1]
    
    return ""

if __name__ == "__main__":
    res = long_palind_sub("abaxyzzyxf")

    assert res == "xyzzyx", res

    print("You're all set!")
